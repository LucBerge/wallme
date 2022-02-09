# coding: utf8

from .. import utils

KEY = 'the-telegraph'
DESCRIPTION = 'Pictures reflecting the political, social or environmental situations in the world'
URL = 'https://www.telegraph.co.uk/pictures-of-the-day/'


def pre_process(subkey):
    return None


def process(date, subkey):
    soup = utils.get_soup_from_url(URL)
    h2s = utils.find_tags_from_soup(soup, "h2", attributes={"class": "u-heading-1"})
    soup = utils.get_soup_from_url("https://www.telegraph.co.uk" + h2s[0].a.get('href'))
    imgs = utils.find_tags_from_soup(soup, "img", attributes={"class": "gallery__regwall-image"})
    return "https://www.telegraph.co.uk" + imgs[0].get('src').split('?')[0]


def post_process(image):
    return None
