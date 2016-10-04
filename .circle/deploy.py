# Licensed to the StackStorm, Inc ('StackStorm') under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import base64
import hashlib
import os
import sys

import requests

EXCHANGE_ORG = 'StackStorm-Exchange'
INDEX_REPO = 'index'
AUTH = (os.environ['MACHINE_USER'], os.environ['MACHINE_PASSWORD'])


def get_file(pack_name):
    url = 'https://api.github.com/repos/{}/{}/contents/index/v1/packs/{}.yaml'.format(
        EXCHANGE_ORG, INDEX_REPO, pack_name
    )

    return requests.get(url)

def put_file(pack_name, content, sha=None):
    url = 'https://api.github.com/repos/{}/{}/contents/index/v1/packs/{}.yaml'.format(
        EXCHANGE_ORG, INDEX_REPO, pack_name
    )

    payload = {
        'message': 'Update {} pack metadata'.format(pack_name),
        'content': base64.b64encode(content),
    }

    if sha:
        payload['sha'] = sha

    return requests.put(url, json=payload, auth=AUTH)

def calculate_git_sha(content):
    sha = hashlib.sha1()
    sha.update('blob {}\0{}'.format(len(content), content))
    return sha.hexdigest()

if __name__ == '__main__':
    local_path = sys.argv[1]
    pack_name = sys.argv[2]

    with file(local_path) as f:
        content = f.read()

    current_pack_meta = get_file(pack_name)

    if current_pack_meta.status_code == 200:
        sha = current_pack_meta.json()['sha']

        if sha != calculate_git_sha(content):
            r = put_file(pack_name, content, sha)
            print('Pack index has been updated with new version of the pack.')
        else:
            print('File is already up to date, skipping...')
    else:
        r = put_file(pack_name, content)
        print('Pack index has been updated with new pack.')
