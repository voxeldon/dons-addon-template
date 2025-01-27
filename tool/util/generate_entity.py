import os
import json
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from index import BP_PATH, RP_PATH

# Load the config.json file
script_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(script_dir, 'config.json')

with open(config_path, 'r') as config_file:
    config = json.load(config_file)

PACK_ID = config['pack_id']
ENGINE_VERSION = config['engine_version']

BP_ENTITY_PATH = os.path.join(BP_PATH, 'entities', PACK_ID)
RP_ENTITY_PATH = os.path.join(RP_PATH, 'entity', PACK_ID)
MODEL_PATH = os.path.join(RP_PATH, 'models', 'entity')

def verify_paths():
    paths = [BP_ENTITY_PATH, RP_ENTITY_PATH, MODEL_PATH]
    for path in paths:
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"{path} created")

verify_paths()

def get_model_ids():
    identifiers = []
    for root, _, files in os.walk(MODEL_PATH):
        for filename in files:
            if filename.endswith('.json'):
                file_path = os.path.join(root, filename)
                with open(file_path, 'r') as file:
                    data = json.load(file)
                    try:
                        identifier = data['minecraft:geometry'][0]['description']['identifier']
                        identifiers.append(identifier)
                    except (KeyError, IndexError):
                        print(f"Identifier not found in {filename}")
    return identifiers

def clean_model_ids(model_ids):
    prefix = "geometry.arcedge."
    return [identifier.replace(prefix, "") for identifier in model_ids]

def generate_entities(entity_names):
    for name in entity_names:
        bp_file_path = os.path.join(BP_ENTITY_PATH, f"{name}.json")
        rp_file_path = os.path.join(RP_ENTITY_PATH, f"{name}.json")

        if os.path.exists(bp_file_path) or os.path.exists(rp_file_path):
            print(f"Skipping {name}: file already exists")
            continue
        
        bp = {
            "format_version": ENGINE_VERSION,
            "minecraft:entity": {
                "description": {
                    "identifier": f"{PACK_ID}:{name}",
                    "is_spawnable": True,
                    "is_summonable": True
                },
                "components": {
                    "minecraft:physics": {},
                    "minecraft:type_family": {"family": [f"{PACK_ID}:{name}"]},
                    "minecraft:damage_sensor": {"triggers": {"cause": "all", "deals_damage": False}},
                    "minecraft:collision_box": {"width": 0.5, "height": 0.5},
                    "minecraft:pushable": {"is_pushable": False, "is_pushable_by_piston": False}
                }
            }
        }

        rp = {
            "format_version": ENGINE_VERSION,
            "minecraft:client_entity": {
                "description": {
                    "identifier": f"{PACK_ID}:{name}",
                    "materials": {
                        "default": "entity_alphatest"
                    },
                    "textures": {
                        "default": f"textures/{PACK_ID}/entity/{name}"
                    },
                    "geometry": {"default": f"geometry.{PACK_ID}.{name}"},
                    "render_controllers": ["controller.render.default"]
                }
            }
        }

        bp_file_path = os.path.join(BP_ENTITY_PATH, f"{name}.json")
        rp_file_path = os.path.join(RP_ENTITY_PATH, f"{name}.json")

        with open(bp_file_path, 'w') as bp_file:
            json.dump(bp, bp_file, indent=4)
            print(f"Created BP entity file: {bp_file_path}")

        with open(rp_file_path, 'w') as rp_file:
            json.dump(rp, rp_file, indent=4)
            print(f"Created RP entity file: {rp_file_path}")

# Prompt the user
user_input = input("Do you want to generate a batch from the model folder? (yes/no): ").strip().lower()

if user_input == 'yes':
    model_ids = get_model_ids()
    entity_names = clean_model_ids(model_ids)
else:
    entity_names_input = input("Enter entity name(s) (comma-separated for multiple): ").strip()
    entity_names = [name.strip() for name in entity_names_input.split(',')]

generate_entities(entity_names)