# coding: utf8

from .. import utils

KEY = 'the-guardian'
DESCRIPTION = 'Each day the picture editor of the Guardian brings you a selection of photo highlights'
URL = 'https://www.theguardian.com/news/series/ten-best-photographs-of-the-day'


def pre_process(subkey):
    return None


def process(date, subkey):
    soup = utils.get_soup_from_url(URL)
    imgs = utils.find_tags_from_soup(soup, "a", attributes={"class": "u-faux-block-link__overlay"})
    soup = utils.get_soup_from_url(imgs[0].get('href'))
    sources = utils.find_tags_from_soup(soup, "source", attributes={"sizes": "1900px"})
    return sources[0].get('srcset').split(' ')[0]


def post_process(image):
    return None
