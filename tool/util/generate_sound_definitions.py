import os
import json
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ..index import RP_PATH, PACK_ID

RP_SOUND_DEFINITIONS_PATH = os.path.join(RP_PATH, 'sounds', 'sound_definitions.json')
RP_SOUNDS_PATH = os.path.join(RP_PATH, 'sounds', PACK_ID)

sound_definitions = {
    "format_version": "1.14.0",
    "sound_definitions": {}
}

def ensure_sound_definitions_file():
    """Ensure the sound definitions file exists."""
    if not os.path.exists(RP_SOUND_DEFINITIONS_PATH):
        os.makedirs(os.path.dirname(RP_SOUND_DEFINITIONS_PATH), exist_ok=True)
        with open(RP_SOUND_DEFINITIONS_PATH, 'w') as f:
            json.dump(sound_definitions, f, indent=4)

def get_all_files(path):
    """Get all file names in the given path and subfolders."""
    file_list = []
    for root, _, files in os.walk(path):
        for file in files:
            relative_path = os.path.relpath(os.path.join(root, file), path)
            file_list.append(relative_path)
    return file_list

def update_sound_definitions(files):
    """Update the sound definitions based on the file names."""
    with open(RP_SOUND_DEFINITIONS_PATH, 'r') as f:
        sound_definitions = json.load(f)

    for file in files:
        file_name = os.path.splitext(os.path.basename(file))[0]
        subfolder_name = os.path.dirname(file)
        
        # Handle root folder separately
        if subfolder_name == '.' or subfolder_name == '':
            key = f"{PACK_ID}.{file_name}"
        else:
            subfolder_name = subfolder_name.replace(os.sep, '_')
            key = f"{PACK_ID}.{subfolder_name}_{file_name}"
        
        # Remove extension from sound_path
        sound_path = f"sounds/{PACK_ID}/{os.path.splitext(file.replace(os.sep, '/'))[0]}"

        sound_definitions["sound_definitions"][key] = {
            "category": "neutral",
            "sounds": [{"name": sound_path, "volume": 1.0}]
        }

    with open(RP_SOUND_DEFINITIONS_PATH, 'w') as f:
        json.dump(sound_definitions, f, indent=4)


def main():
    ensure_sound_definitions_file()
    files = get_all_files(RP_SOUNDS_PATH)
    update_sound_definitions(files)
    for file in files:
        print(f'Generated defenition: {file}')

if __name__ == "__main__":
    main()
