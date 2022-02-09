# coding: utf8

from .. import utils
from ..exceptions import WallmeException
import datetime

KEY = 'apod'
DESCRIPTION = 'Astronomy Picture Of the Day'
URL = 'https://apod.nasa.gov/apod/astropix.html'


def pre_process(subkey):
    return None


def process(date, subkey):
    soup = utils.get_soup_from_url(URL)
    try:
        imgs = utils.find_tags_from_soup(soup, "img")
    except Exception:
        try:
            print('Could not find today\'s picture, getting yesterday\'s one')
            date = date - datetime.timedelta(days=1)
            soup = utils.get_soup_from_url('https://apod.nasa.gov/apod/ap' + date.strftime("%y%m%d") + '.html')
            imgs = utils.find_tags_from_soup(soup, "img")
        except Exception:
            raise WallmeException('No picture found today neither yesterday. It could be a video.')

    return 'https://apod.nasa.gov/apod/' + imgs[0].get('src')


def post_process(image):
    return None
