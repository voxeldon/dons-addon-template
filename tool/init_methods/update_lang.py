import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from index import BP_PATH, RP_PATH, AUTHOR, PACK_ID

BP_LANG_PATH = os.path.join(BP_PATH, 'texts/en_US.lang')
RP_LANG_PATH = os.path.join(RP_PATH, 'texts/en_US.lang')

def update_lang_file(file_path, pack_name):
    with open(file_path, 'r') as file:
        content = file.read()
    
    lines = content.splitlines()
    updated_lines = []
    for line in lines:
        if line.startswith('pack.name='):
            line = f'pack.name={pack_name}'
        elif line.startswith('pack.description='):
            line = f'pack.description={pack_name}'
        updated_lines.append(line)
    
    updated_content = '\n'.join(updated_lines)
    
    with open(file_path, 'w') as file:
        file.write(updated_content)

def update_lang():
    update_lang_file(BP_LANG_PATH, f"{AUTHOR}'s {PACK_ID}")
    update_lang_file(RP_LANG_PATH, f"{AUTHOR}'s {PACK_ID}")
    print(f"Lang files updated.")
