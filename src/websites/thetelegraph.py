# coding: utf8

from .. import utils

KEY = 'the-telegraph'
TEST_KEY = KEY
DESCRIPTION = 'Pictures reflecting the political, social or environmental situations in the world'
URL = 'https://www.telegraph.co.uk/news/pictures/'


def pre_process(subkey):
    return None


def process(date, subkey):
    soup = utils.get_soup_from_url(URL)
    h3s = utils.find_tags_from_soup(soup, "h3", attributes={"class": "u-heading-6"})
    soup = utils.get_soup_from_url("https://www.telegraph.co.uk" + h3s[0].a.get('href'))
    imgs = utils.find_tags_from_soup(soup, "img", attributes={"class": "gallery__regwall-image"})
    return "https://www.telegraph.co.uk" + imgs[0].get('src').split('?')[0]


def post_process(image):
    return None
