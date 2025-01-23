import os
import json

parent_dir = os.path.dirname(os.path.dirname(__file__))
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

def update_files(pack_id, author):
    update_name(package_lock_path, pack_id)
    update_name(package_json_path, pack_id)
    update_author(package_json_path, author)
    update_name(config_path, pack_id)
    update_author(config_path, author)
    new_outdir = f"./packs/bp/scripts/{pack_id}"
    update_outdir(tsconfig_path, new_outdir)
    print('Config files updated.')
