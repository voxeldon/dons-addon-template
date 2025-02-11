import json
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from index import RP_PATH, OUTPUT_PATH
PARTICLES_PATH = os.path.join(RP_PATH, "particles")
OUTPUT_FILE = os.path.join(OUTPUT_PATH, "particle_definitions_enum.ts")

def get_particle_identifiers(particles_path):
    identifiers = {}
    for root, _, files in os.walk(particles_path):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    data = json.load(f)
                    try:
                        identifier = data['particle_effect']['description']['identifier']
                        enum_key = identifier.split(':')[-1].replace('_', ' ').title().replace(' ', '')
                        identifiers[enum_key] = identifier
                    except KeyError:
                        continue
    return identifiers

def generate_enum_file(identifiers, output_file):
    with open(output_file, 'w') as f:
        f.write('export enum ParticleDefinitions {\n')
        for key, value in identifiers.items():
            f.write(f'    {key} = "{value}",\n')
        f.write('}\n')

if __name__ == "__main__":
    identifiers = get_particle_identifiers(PARTICLES_PATH)
    generate_enum_file(identifiers, OUTPUT_FILE)