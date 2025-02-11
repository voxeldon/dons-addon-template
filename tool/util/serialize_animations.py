import os
import json
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from index import RP_PATH, ROOT_PATH, OUTPUT_PATH

def read_json_files(folder_path, output_folder):
    was_format_invalid = False
    result = {}
    json_file_count = 0
    
    for root, _, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith(".json"):
                json_file_count += 1
                file_path = os.path.join(root, file_name)
                try:
                    with open(file_path, "r", encoding="utf-8") as file:
                        data = json.load(file)
                    
                    # Extract animations
                    animations = data.get("animations", {})
                    for anim_key, anim_data in animations.items():
                        parts = anim_key.split(".")
                        if len(parts) >= 3:
                            entity_name = parts[2].split("_")[0]
                            animation_name = "_".join(parts[2].split("_")[1:])
                            
                            if not animation_name:
                                print(f"Invalid animation format: {anim_key}")
                                was_format_invalid = True
                                continue
                            
                            loop_value = anim_data.get("loop", False)
                            if loop_value == "hold_on_last_frame":
                                loop_value = True
                            
                            # Group animations under the entity name
                            if entity_name not in result:
                                result[entity_name] = {}
                            
                            result[entity_name][animation_name] = {
                                "typeId": anim_key,
                                "loop": loop_value,
                                "animation_length": anim_data.get("animation_length", 0)
                            }
                        else:
                            print(f"Invalid animation format: {anim_key}")
                except (json.JSONDecodeError, KeyError, TypeError) as e:
                    print(f"Error reading {file_name}: {e}")
    
    # Ensure the output directory exists
    os.makedirs(output_folder, exist_ok=True)
    
    # Print the result
    if json_file_count > 0:
        if was_format_invalid: print("Use format: animation.pack_id.entity_name_action_subaction i.e(animation.foo.pig_walk_fast)")
        print(f"Serialized {json_file_count} animation files.")
    else:
        print("No animation files found.")
        return

    # Write the result to a TypeScript file
    output_path = os.path.join(output_folder, "animation_data.ts")
    with open(output_path, "w", encoding="utf-8") as output_file:
        output_file.write("const ANIMATION_DATA: { [key: string]: { [key: string]: {typeId: string; loop: boolean; animation_length: number; } } } = ")
        json.dump(result, output_file, indent=4)
        output_file.write(";\n")

if __name__ == "__main__":
    base_folder = ROOT_PATH
    folder_path = os.path.join(RP_PATH, "animations")
    read_json_files(folder_path, OUTPUT_PATH)