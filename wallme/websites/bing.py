# coding: utf8

from .. import utils

KEY = 'bing'
DESCRIPTION = 'Various landscapes taken from the web search engine Bing'
URL = 'http://www.bing.com'


def pre_process(subkey):
    return None


def process(date, subkey):
    json = utils.get_json_from_url('http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=EN-IN')
    return "https://www.bing.com" + json['images'][0]['url']


def post_process(image):
    return None
