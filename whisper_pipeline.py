import argparse
import os
import re
import whisper

def parse_utsdata(file_path):
    """Parses a .utsdata file and returns a dictionary mapping strings to keys, and keys to strings."""
    key_to_string = {}
    string_to_key = {}

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    current_key = None
    current_value = []

    for line in lines:
        line = line.strip()
        if not line or line.startswith('//') or line.startswith('$'):
            continue

        if line.startswith('@') and not line.startswith('@@:'):
            if current_key:
                val = '\n'.join(current_value)
                key_to_string[current_key] = val
                string_to_key[val] = current_key

            parts = line.split(':', 1)
            if len(parts) == 2:
                current_key = parts[0]
                current_value = [parts[1]]
        elif line.startswith('@@:'):
            parts = line.split(':', 1)
            if len(parts) == 2 and current_key:
                current_value.append(parts[1])

    if current_key:
        val = '\n'.join(current_value)
        key_to_string[current_key] = val
        string_to_key[val] = current_key

    return key_to_string, string_to_key

def clean_text(text):
    """Normalize text for matching by removing punctuation and converting to lowercase."""
    text = re.sub(r'[^\w\s]', '', text)
    return text.lower().strip()

def main():
    parser = argparse.ArgumentParser(description="Transcribe audio with Whisper and translate using Alinit UTS dictionaries.")
    parser.add_argument("audio_file", help="Path to the audio file to transcribe")
    parser.add_argument("target_lang", help="Target language code (e.g., ko-kr, ja-jp)")
    parser.add_argument("--model", default="base", help="Whisper model size to use (default: base)")
    parser.add_argument("--hub_dir", default="AG_SubSim_Unlimited_Hub", help="Path to the Hub directory")

    args = parser.parse_args()

    english_dict_path = os.path.join(args.hub_dir, "Translations", "en-us.utsdata")
    target_dict_path = os.path.join(args.hub_dir, "Translations", f"{args.target_lang}.utsdata")

    if not os.path.exists(english_dict_path):
        print(f"Error: English dictionary not found at {english_dict_path}")
        return

    if not os.path.exists(target_dict_path):
        print(f"Error: Target dictionary not found at {target_dict_path}")
        return

    print(f"Loading dictionaries...")
    en_key_to_str, en_str_to_key = parse_utsdata(english_dict_path)
    tgt_key_to_str, tgt_str_to_key = parse_utsdata(target_dict_path)

    # Create normalized mapping
    normalized_en_to_key = {clean_text(k): v for k, v in en_str_to_key.items()}

    print(f"Loading Whisper model '{args.model}'...")
    try:
        model = whisper.load_model(args.model)
    except Exception as e:
        print(f"Error loading Whisper model: {e}")
        print("Please ensure openai-whisper is installed: pip install openai-whisper")
        return

    print(f"Transcribing {args.audio_file}...")
    result = model.transcribe(args.audio_file)

    print("\n--- Transcription & Translation ---")

    for segment in result["segments"]:
        text = segment["text"].strip()
        print(f"Original: {text}")

        # Try to find an exact match first, then normalized match
        translated = None
        key = en_str_to_key.get(text)

        if not key:
            normalized_text = clean_text(text)
            key = normalized_en_to_key.get(normalized_text)

        if key and key in tgt_key_to_str:
            translated = tgt_key_to_str[key]
            print(f"Translated ({args.target_lang}): {translated}")
        else:
            print(f"Translated ({args.target_lang}): [No match found in dictionary]")
        print("-" * 30)

if __name__ == "__main__":
    main()
