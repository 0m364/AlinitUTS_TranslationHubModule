Help to translate AG Subway Simulator Unlimited! Credits will be provided in the "About" section. Email us for more information: support@alinit.org

# AlinitUTS_TranslationHubModule
Alinit UTS Translation Hub module (preview version). This repository provides a sample dictionary for custom translations.
The module currently integrated with AG Subway Simulator Unlimited (version 1.3.5 and higher) and [AG Subway Simulator 2](https://play.google.com/store/apps/details?id=com.AlinitProject.AGSubSim2).

Translation file description available here: https://uts.alinit.org/docs/alinit-uts-translation-hub-module/

If you want to make your own translation dictionary for AG Subway Simulator Unlimited, please contact support: support@alinit.org

**Repository Structure**
```
AlinitUTS_TranslationHubModule
\
 |-[GAME_OR_PROJECT_NAME]_HUB
  \
   |-Translations //folder, contains translation files 
   |-Version //folder, contains version info file
   |-README.md //this readme file
```


**Auto-generated translations** marked as "[AUTO]". It means that the translation is generated using the machine translation service.
List of auto-generated translations (translations that may need improvement):

- [ko-kr (Korean)](https://github.com/nitro577/AlinitUTS_TranslationHubModule/blob/main/Translations/ko-kr.utsdata)
- [ja-jp (Japanese)](https://github.com/nitro577/AlinitUTS_TranslationHubModule/blob/main/Translations/ja-jp.utsdata)

German translation provided by [@Janikfrb](https://github.com/Janikfrb)

Czech translation provided by [@falconczfi](https://github.com/falconczfi)

French translation edited by [@ben20471](https://github.com/ben20471)

Spanish translation provided by [@Rescue742Fan](https://github.com/Rescue742Fan)

---

## OpenAI Whisper Translation Pipeline

This repository includes a preconfigured Python pipeline to easily translate audio speech using the `.utsdata` dictionaries and **OpenAI Whisper**. The script transcribes spoken English audio and maps it to the existing translated dictionary keys to output translations.

### Requirements

To use the transcription pipeline, make sure to install the dependencies:

```bash
pip install -r requirements.txt
```

Note: You may also need to install `ffmpeg` on your system.
- On Ubuntu/Debian: `sudo apt update && sudo apt install ffmpeg`
- On MacOS (using Homebrew): `brew install ffmpeg`

### Usage

Run the `whisper_pipeline.py` script and pass in your audio file and the target language code. For example, to translate to Japanese (`ja-jp`):

```bash
python whisper_pipeline.py path/to/audio.mp3 ja-jp
```

The script will transcribe the audio, map it to the dictionary's English strings, and print out the corresponding Japanese localized text.

### Licensing

OpenAI Whisper is distributed under the MIT License. See `OPENAI_WHISPER_LICENSE` for more details.
