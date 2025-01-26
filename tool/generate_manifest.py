import ast
import uuid
import json
import os
from index import BP_PATH, RP_PATH
from update_config_files import update_files
from update_lang import update_lang
from write_config import write_config

AUTHOR = 'unknown_author'
PACK_ID = 'addon_template'
VERSION = [0, 0, 0]
ENGINE_VERSION = [1, 21, 41]
API_VERSION = "1.16.0"
UI_API_VERSION = "1.3.0"

def generate_uuid():
    return str(uuid.uuid4())

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

BPUUID1 = generate_uuid()
BPUUID2 = generate_uuid()
BPUUID3 = generate_uuid()
RPUUID1 = generate_uuid()
RPUUID2 = generate_uuid()

BP_MANIFEST = {
  "format_version": 2,
  "header": {
    "description": "pack.description",
    "name": "pack.name",
    "uuid": f"{BPUUID1}",
    "version": VERSION,
    "min_engine_version": ENGINE_VERSION
  },
  "modules": [
    {"type": "data", "uuid": f"{BPUUID2}", "version": VERSION},
    {
      "type": "script",
      "language": "javascript",
      "uuid": f"{BPUUID3}",
      "version": VERSION,
      "entry": f"scripts/{PACK_ID}/index.js"
    }
  ],
  "metadata": {"authors": [AUTHOR]},
  "dependencies": [
    {"uuid": f"{RPUUID1}", "version": VERSION},
    {"module_name": "@minecraft/server", "version": f"{API_VERSION}"},
    {"module_name": "@minecraft/server-ui", "version": f"{UI_API_VERSION}"}
  ]
}

RP_MANIFEST = {
  "format_version": 2,
  "header": {
    "description": "pack.description",
    "name": "pack.name",
    "uuid": f"{RPUUID1}",
    "version": VERSION,
    "min_engine_version": [1, 20, 81]
  },
  "modules": [
    {"type": "resources", "uuid": f"{RPUUID2}", "version": VERSION}
  ],
  "dependencies": [
    {"uuid": f"{BPUUID1}", "version": VERSION}
  ],
  "metadata": {"authors": [AUTHOR]}
}

# Ensure BP_PATH and RP_PATH are directories and specify filenames
BP_FILE_PATH = os.path.join(BP_PATH, 'manifest.json')
RP_FILE_PATH = os.path.join(RP_PATH, 'manifest.json')

# Write BP_MANIFEST to BP_FILE_PATH
with open(BP_FILE_PATH, 'w') as bp_file:
    json.dump(BP_MANIFEST, bp_file, indent=4)

# Write RP_MANIFEST to RP_FILE_PATH
with open(RP_FILE_PATH, 'w') as rp_file:
    json.dump(RP_MANIFEST, rp_file, indent=4)

print(f"Generated manifest files.")

update_files(PACK_ID, AUTHOR)
update_lang(f"{AUTHOR}'s {PACK_ID}")
write_config(PACK_ID, VERSION, ENGINE_VERSION, API_VERSION, UI_API_VERSION)

print(f"Addon ready!")