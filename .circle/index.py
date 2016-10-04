import os
import json
import yaml
import sys
from glob import glob


def build_index(path):
    packs = {}
    for filename in glob('%s/packs/*.yaml' % path):
      with open(filename, 'r') as pack:
        pack_meta = yaml.load(pack)
        packs[pack_meta['name']] = pack_meta 
    with open('%s/index.json' % path, 'w') as outfile:
        json.dump(packs, outfile)

if __name__ == '__main__':
    path = sys.argv[1]
    build_index(path)
