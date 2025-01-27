import os
import json
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from index import BP_PATH, RP_PATH

BP_FILE_PATH = os.path.join(BP_PATH, 'manifest.json')
RP_FILE_PATH = os.path.join(RP_PATH, 'manifest.json')

SET_VERSION = None

def increment_version(version):
    # Increment the last number in the version array
    version[-1] += 1
    global SET_VERSION
    if SET_VERSION is None:
        SET_VERSION = version.copy()
    return version

def update_versions(manifest):
    if isinstance(manifest, dict):
        for key, value in manifest.items():
            if key == "version" and isinstance(value, list):
                manifest[key] = increment_version(value)
            else:
                update_versions(value)
    elif isinstance(manifest, list):
        for item in manifest:
            update_versions(item)

def load_json(file_path):
    if not os.path.exists(file_path):
        print(f"No manifest found for {file_path}")
        return None
    with open(file_path, 'r') as file:
        return json.load(file)

def save_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Load the BP and RP manifests
bp_manifest = load_json(BP_FILE_PATH)
rp_manifest = load_json(RP_FILE_PATH)

# Update the versions in the manifests if they were loaded
if bp_manifest:
    update_versions(bp_manifest)
    save_json(BP_FILE_PATH, bp_manifest)

if rp_manifest:
    update_versions(rp_manifest)
    save_json(RP_FILE_PATH, rp_manifest)

if SET_VERSION:
    print(f"Updated manifest version to {SET_VERSION}")