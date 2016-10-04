import os
import json
import yaml
from glob import glob


def build_index(path):
    packs = {}
    for filename in glob('%s/packs/*.yaml' % path):
      with open(filename, 'r') as pack:
        packs.append(yaml.load(pack))
    with open('%s/index.json' % path, 'w') as outfile:
        json.dump(packs, outfile)

if __name__ == '__main__':
    path = sys.argv[1]
    build_index(path)
