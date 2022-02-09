# coding: utf8

from .. import utils

KEY = 'outdoor-photographer'
DESCRIPTION = 'Outdoor pictures, essentially animals and landscapes'
URL = 'https://www.outdoorphotographer.com/blog/category/photo-of-the-day/'


def pre_process(subkey):
    return None


def process(date, subkey):
    soup = utils.get_soup_from_url(URL)
    imgs = utils.find_tags_from_soup(soup, "img", attributes={"class": "wp-post-image"})
    links = imgs[0].get('data-lazy-srcset')
    return links.split(', ')[-1].split(' ')[-2]


def post_process(image):
    return None
