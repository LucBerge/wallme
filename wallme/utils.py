# coding: utf8

import requests
import json
import os
from bs4 import BeautifulSoup
from .exceptions import WallmeException

headers = {'User-Agent': 'Wallme-Bot/1.0'}


def get_webpage_from_url(url):
    try:
        webpage = requests.get(url, headers=headers)
    except requests.exceptions.ConnectionError:
        raise WallmeException("Cannot retrieve webpage '" + url + "'. Make sure you have an internet connection, retry later.")
    if webpage.status_code == 429:
        raise WallmeException("Cannot retrieve webpage '" + url + "' (error " + str(webpage.status_code) + "). Too many requests, retry later.")
    if webpage.status_code != 200:
        raise Exception("Cannot retrieve webpage '" + url + "' (error " + str(webpage.status_code) + "). Please make sure the url is valid.")
    return webpage.text


def get_json_from_url(url):
    return json.loads(get_webpage_from_url(url))


def get_soup_from_url(url, parser='html.parser'):
    return BeautifulSoup(get_webpage_from_url(url), parser)


def find_tags_from_soup(soup, tag, attributes=None):
    if(attributes):
        tags = soup.findAll(tag, attributes)
    else:
        tags = soup.find_all(tag)
    if(len(tags) == 0):
        raise Exception("Couldn't find tag '" + tag + "' with attributes '" + str(attributes) + "'.")
    return tags


def get_key_subkey_from_fullkey(fullkey):
    dot_index = fullkey.find('.')
    if dot_index > 0:
        return fullkey[:dot_index], fullkey[dot_index + 1:]
    else:
        return fullkey, None


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
