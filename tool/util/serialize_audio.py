import json
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from index import RP_PATH, ROOT_PATH, OUTPUT_PATH
JSON_PATH = os.path.join(RP_PATH, "sounds/sound_definitions.json")
OUTPUT_FILE = os.path.join(OUTPUT_PATH, "sound_definitions_enum.ts")

def format_enum_key(key):
    key = key.replace("ss_ele.", "")
    parts = key.replace(".", "_").split("_")
    return "".join(part.capitalize() for part in parts)

def main():

    os.makedirs(OUTPUT_PATH, exist_ok=True)

    with open(JSON_PATH, "r") as json_file:
        data = json.load(json_file)

    sound_definitions = data.get("sound_definitions", {})

    enum_lines = ["export enum SoundDefinitions {"]
    for key in sound_definitions.keys():
        enum_key = format_enum_key(key)
        enum_lines.append(f"    {enum_key} = '{key}',")
    enum_lines.append("}")

    with open(OUTPUT_FILE, "w") as output_file:
        output_file.write("\n".join(enum_lines))

    print(f"Enum file generated at: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
