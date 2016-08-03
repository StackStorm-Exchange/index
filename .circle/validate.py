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

import sys

import jsonschema
import yaml

def load_yaml_file(path):
    with file(path, 'r') as stream:
        text = yaml.load(stream)

    return text

def validate_schema(instance, schema):
    return jsonschema.validate(instance, schema)

def validate_repo_name(instance, repo_name):
    if pack_meta['name'] != repo_name:
        raise ValueError('Pack name is different from repository name.')

if __name__ == '__main__':
    repo_name = sys.argv[1]
    pack_meta = load_yaml_file(sys.argv[2])
    pack_schema = load_yaml_file(sys.argv[3])

    validate_schema(pack_meta, pack_schema)
    validate_repo_name(pack_meta, repo_name)
