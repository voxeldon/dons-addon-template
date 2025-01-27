import ast
from generate_manifest import generate_manifest
from update_config_files import update_files
from update_lang import update_lang
from write_config import write_config

AUTHOR = 'unknown_author'
PACK_ID = 'addon_template'
VERSION = [0, 0, 0]
ENGINE_VERSION = [1, 21, 41]
API_VERSION = "1.16.0"
UI_API_VERSION = "1.3.0"

def update_config(config):
    global AUTHOR, PACK_ID, VERSION, ENGINE_VERSION, API_VERSION, UI_API_VERSION
    
    if 'author' in config:
        AUTHOR = config['author']
    if 'pack_id' in config:
        PACK_ID = config['pack_id']
    if 'version' in config:
        VERSION = config['version']
    if 'engine_version' in config:
        ENGINE_VERSION = config['engine_version']
    if 'api_version' in config:
        API_VERSION = config['api_version']
    if 'ui_api_version' in config:
        UI_API_VERSION = config['ui_api_version']

# Prompt the user for input
user_input = input("Enter the configuration dictionary or press enter to use defaults.\n(e.g., {'author': 'me', 'pack_id': 'test'}): ")

# Parse the input as a dictionary if provided
if user_input.strip():
    try:
        config = ast.literal_eval(user_input)
        if isinstance(config, dict):
            update_config(config)
        else:
            print("Invalid input. Please enter a valid dictionary.")
    except (ValueError, SyntaxError):
        print("Invalid input. Please enter a valid dictionary.")

write_config(AUTHOR, PACK_ID, VERSION, ENGINE_VERSION, API_VERSION, UI_API_VERSION)
update_files()
generate_manifest()
update_lang()

print(f"Addon ready!")