import requests, json
from bs4 import BeautifulSoup
from .exceptions import WallmeException

headers = {'User-agent': 'wallme'}

def get_webpage_from_url(url):
    try:
        webpage = requests.get(url, headers=headers)
    except requests.exceptions.ConnectionError as e:
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