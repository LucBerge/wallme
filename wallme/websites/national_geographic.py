# coding: utf8

from .. import utils

KEY = 'national-geographic'
DESCRIPTION = 'The National-Geographic magazine gives you pictures about live on earth'
URL = 'https://www.nationalgeographic.com/photo-of-the-day/'


def pre_process(subkey):
    return None


def process(date, subkey):
    soup = utils.get_soup_from_url(URL)
    images = utils.find_tags_from_soup(soup, "meta", attributes={"property": "og:image"})
    return images[0].get('content')


def post_process(image):
    return None
