# coding: utf8

from .website import Website
from ..exceptions import WallmeException


class Reddit(Website):
    key = 'reddit'
    description = 'Top pictures from the topic of your choice. Use \"reddit.<subreddit>\" as the key. (e.g.: reddit.earthporn)'
    url = 'http://www.reddit.com/r/'

    def pre_process(self, subkey):
        if(subkey is None):
            raise WallmeException('You must specify the subreddit: "reddit.<subreddit>" (e.g.: reddit.earthporn)')

    def process(self, date, subkey):
        json = self.get_json_from_url('http://www.reddit.com/r/' + subkey + '/top/.json?limit=100')
        for children in json['data']['children']:
            if("i.redd.it" in children['data']['url']):
                return children['data']['url']
        raise WallmeException("No image found today...")
