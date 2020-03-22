import requests, json
from bs4 import BeautifulSoup

def get_webpage_from_url(url):
	webpage = requests.get(url)
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