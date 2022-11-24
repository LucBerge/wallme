# coding: utf8

import json
import os
from .websites import WEBSITES
from .exceptions import WallmeException


def get_key_subkey_from_fullkey(full_key):
    dot_index = full_key.find('.')
    if dot_index > 0:
        return full_key[:dot_index], full_key[dot_index + 1:]
    else:
        return full_key, None


def get_website_from_key(key):
    if(key not in WEBSITES.keys()):
        raise WallmeException("Website '" + key + "' not supported. Use the -list option to list all the posibilities.")
    return WEBSITES[key]


def get_website_subkey_from_fullkey(full_key):
    key, subkey = get_key_subkey_from_fullkey(full_key)
    website = get_website_from_key(key)
    return website, subkey


def read_json(file_name):
    if(not os.path.isfile(file_name)):
        raise Exception('File ' + file_name + ' does not exist. Build it first.')
    file = open(file_name, 'r')
    data = json.loads(file.read())
    file.close()
    return data


def save_json(file_name, data):
    file = open(file_name, 'w')
    file.write(json.dumps(data))
    file.close()
