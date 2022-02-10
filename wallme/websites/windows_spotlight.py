# coding: utf8

from .. import utils

KEY = 'windows-spotlight'
DESCRIPTION = 'High resolution quality images from Windows 10 Spotlight'
URL = 'https://windows10spotlight.com/'


def pre_process(subkey):
    return None


def process(date, subkey):
    soup = utils.get_soup_from_url(URL)
    imgs = utils.find_tags_from_soup(soup, "img", attributes={"class": "thumbnail wp-post-image"})
    links = imgs[0].get('srcset')
    return links.split(', ')[-1].split(' ')[-2]


def post_process(image):
    return None
