# coding: utf8

from .. import utils

KEY = 'wikipedia'
TEST_KEY = KEY
DESCRIPTION = 'English wikipedia picture of the day, mostly about history'
URL = 'https://en.wikipedia.org/wiki/Wikipedia:Picture_of_the_day'


def pre_process(subkey):
    return None


def process(date, subkey):
    soup = utils.get_soup_from_url(URL)
    imgs = utils.find_tags_from_soup(soup, "img")
    current_width = imgs[0].get('width')
    full_width = imgs[0].get('data-file-width')
    return "https:" + imgs[0].get('src').replace(str(current_width + "px"), str(full_width + "px"))


def post_process(image):
    return None
