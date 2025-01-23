import os

from index import BP_PATH, RP_PATH

BP_LANG_PATH = os.path.join(BP_PATH, 'texts/en_US.lang')
RP_LANG_PATH = os.path.join(RP_PATH, 'texts/en_US.lang')


def update_lang_file(file_path, pack_name):
    with open(file_path, 'r') as file:
        content = file.read()
    
    content = content.replace('pack.name=Addon Template', f'pack.name={pack_name}')
    content = content.replace('pack.description=Addon Template', f'pack.description={pack_name}')
    
    with open(file_path, 'w') as file:
        file.write(content)

def update_lang(pack_name):
    update_lang_file(BP_LANG_PATH, f'{pack_name}')
    update_lang_file(RP_LANG_PATH, f'{pack_name}')
    print(f"Lang files updated.")
