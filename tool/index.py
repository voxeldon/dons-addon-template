import os
import json

#Index
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)
parent_dir = os.path.dirname(script_dir)
config_path = os.path.join(script_dir, 'config.json')
with open(config_path, 'r') as config_file:
    config = json.load(config_file)

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PACKS_PATH = os.path.join(parent_dir, 'packs')
BP_PATH = os.path.join(PACKS_PATH, 'BP')
RP_PATH = os.path.join(PACKS_PATH, 'RP')
OUTPUT_PATH = os.path.join(ROOT_PATH, "tool", "output")

AUTHOR = config['author']
PACK_ID = config['pack_id']
VERSION = config['version']
ENGINE_VERSION = config['engine_version']
API_VERSION = config['api_version']
UI_API_VERSION = config['ui_api_version']