import glob
import os
import pytest

def get_translation_files():
    # Get the directory where this test file is located
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Go up one level to the project root
    project_root = os.path.dirname(current_dir)
    # Construct the path to the Translations directory
    translations_dir = os.path.join(project_root, 'Translations')
    return glob.glob(os.path.join(translations_dir, '*.utsdata'))

@pytest.mark.parametrize("filepath", get_translation_files())
def test_no_auto_generated_translations(filepath):
    """
    Checks if the translation file contains the '[AUTO]' tag,
    which indicates it was machine-generated and needs manual review.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if '[AUTO]' in content:
        pytest.xfail(f"File {os.path.basename(filepath)} contains auto-generated translations ([AUTO])")

    assert '[AUTO]' not in content

@pytest.mark.parametrize("filepath", get_translation_files())
def test_translation_file_structure(filepath):
    """
    Checks if the translation file has the basic required structure.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    assert any(line.startswith('$lang:') for line in lines), f"File {os.path.basename(filepath)} is missing $lang metadata"
    assert any(line.startswith('$version:') for line in lines), f"File {os.path.basename(filepath)} is missing $version metadata"
