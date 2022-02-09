# coding: utf8

from .. import utils

KEY = 'wikipedia'
DESCRIPTION = 'English wikipedia picture of the day, mostly about history'
BASE_URL = "https://en.wikipedia.org"
URL = BASE_URL + "/wiki/Wikipedia:Picture_of_the_day"


def pre_process(subkey):
    return None


def process(date, subkey):
    soup = utils.get_soup_from_url(URL)
    links = utils.find_tags_from_soup(soup, "a", attributes={"class": "image"})
    soup = utils.get_soup_from_url(BASE_URL + links[0].get('href'))
    divs = utils.find_tags_from_soup(soup, "div", attributes={"class": "fullImageLink"})
    return "https:" + divs[0].a.get('href')


def post_process(image):
    return None
