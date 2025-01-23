import os
#Index
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)
parent_dir = os.path.dirname(script_dir)

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PACKS_PATH = os.path.join(parent_dir, 'packs')
BP_PATH = os.path.join(PACKS_PATH, 'BP')
RP_PATH = os.path.join(PACKS_PATH, 'RP')
OUTPUT_PATH = os.path.join(ROOT_PATH, "tool", "output")
