from ..exceptions import WallmeException
import requests
import json
from bs4 import BeautifulSoup


class Website():
    HEADERS = {'User-Agent': 'Wallme-Bot/1.0'}

    def pre_process(self, subkey):
        return None

    def post_process(self, image):
        return None

    def get_webpage_from_url(self, url):
        try:
            webpage = requests.get(url, headers=self.HEADERS)
        except requests.exceptions.ConnectionError:
            raise WallmeException("Cannot retrieve webpage '" + url + "'. Make sure you have an internet connection, retry later.")
        if (webpage.status_code == 429):
            raise WallmeException("Cannot retrieve webpage '" + url + "' (error " + str(webpage.status_code) + "). Too many requests, retry later.")
        if (webpage.status_code != 200):
            raise Exception("Cannot retrieve webpage '" + url + "' (error " + str(webpage.status_code) + "). Please make sure the url is valid.")
        return webpage.text

    def get_json_from_url(self, url):
        return json.loads(self.get_webpage_from_url(url))

    def get_soup_from_url(self, url, parser='html.parser'):
        return BeautifulSoup(self.get_webpage_from_url(url), parser)

    def find_tags_from_soup(self, soup, tag, attributes=None):
        if (attributes):
            tags = soup.findAll(tag, attributes)
        else:
            tags = soup.find_all(tag)
        if (len(tags) == 0):
            raise Exception("Couldn't find tag '" + tag + "' with attributes '" + str(attributes) + "'.")
        return tags
