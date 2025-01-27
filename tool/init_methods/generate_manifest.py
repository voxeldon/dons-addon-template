import uuid
import json
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from index import BP_PATH, RP_PATH, AUTHOR, PACK_ID, VERSION, ENGINE_VERSION, API_VERSION, UI_API_VERSION

def generate_uuid():
    return str(uuid.uuid4())

def generate_manifest():
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