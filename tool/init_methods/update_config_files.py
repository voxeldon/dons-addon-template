import os
import json
import sys
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from index import  AUTHOR, PACK_ID , parent_dir

package_lock_path = os.path.join(parent_dir, 'package-lock.json')
package_json_path = os.path.join(parent_dir, 'package.json')
tsconfig_path = os.path.join(parent_dir, 'tsconfig.json')
config_path = os.path.join(parent_dir, 'config.json')

def update_name(file_path, new_name):
    with open(file_path, 'r') as file:
        content = json.load(file)

    content['name'] = new_name

    with open(file_path, 'w') as file:
        json.dump(content, file, indent=2)

def update_author(file_path, new_author):
    with open(file_path, 'r') as file:
        content = json.load(file)

    content['author'] = new_author

    with open(file_path, 'w') as file:
        json.dump(content, file, indent=2)

def update_outdir(file_path, new_outdir):
    with open(file_path, 'r') as file:
        content = json.load(file)

    content['compilerOptions']['outDir'] = new_outdir

    with open(file_path, 'w') as file:
        json.dump(content, file, indent=2)

def update_files():
    update_name(package_lock_path, PACK_ID)
    update_name(package_json_path, PACK_ID)
    update_author(package_json_path, AUTHOR)
    update_name(config_path, PACK_ID)
    update_author(config_path, AUTHOR)
    new_outdir = f"./packs/bp/scripts/{PACK_ID}"
    update_outdir(tsconfig_path, new_outdir)
    print('Config files updated.')
