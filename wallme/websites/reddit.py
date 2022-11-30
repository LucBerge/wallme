# coding: utf8

from .website import Website
from ..exceptions import WallmeException


class Reddit(Website):
    key = 'reddit'
    description = 'Top pictures from the topic of your choice. Use \"reddit.<subreddit>\" as the key. (e.g.: reddit.earthporn)'
    base_url = 'http://www.reddit.com/r/'

    def pre_process(self, subkey):
        if (subkey is None):
            raise WallmeException('You must specify the subreddit: "reddit.<subreddit>" (e.g.: reddit.earthporn)')
        self.info_url = self.base_url + subkey

    def process(self, date, subkey):
        json = self.get_json_from_url(self.info_url + '/top/.json?limit=100')
        for children in json['data']['children']:
            if ("i.redd.it" in children['data']['url']):
                return children['data']['url']
        raise WallmeException("No image found today...")
