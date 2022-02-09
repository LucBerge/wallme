# coding: utf8

from .. import utils
from ..exceptions import WallmeException

KEY = 'reddit'
DESCRIPTION = 'Top pictures from the topic of your choice. Use \"reddit.<subreddit>\" as the key. (e.g. : reddit.earthporn)'
URL = 'http://www.reddit.com/r/'


def pre_process(subkey):
    None


def process(date, subkey):
    json = utils.get_json_from_url('http://www.reddit.com/r/' + subkey + '/top/.json?limit=100')
    for children in json['data']['children']:
        if("i.redd.it" in children['data']['url']):
            return children['data']['url']
    raise WallmeException("No image found today...")


def post_process(image):
    return None
