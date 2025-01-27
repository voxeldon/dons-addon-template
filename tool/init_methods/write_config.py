import json
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from index import script_dir

def write_config(AUTHOR, PACK_ID, VERSION, ENGINE_VERSION, API_VERSION, UI_API_VERSION):
    config = {
        "author": AUTHOR,
        "pack_id": PACK_ID,
        "version": VERSION,
        "engine_version": ENGINE_VERSION,
        "api_version": API_VERSION,
        "ui_api_version": UI_API_VERSION
    }
    
    # Define the path to the config.json file
    config_path = os.path.join(script_dir, 'config.json')
    
    # Write the config dictionary to the config.json file
    with open(config_path, 'w') as config_file:
        json.dump(config, config_file, indent=4)
