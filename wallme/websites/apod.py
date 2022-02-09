# coding: utf8

from .. import utils
from ..exceptions import WallmeException
import datetime

KEY = 'apod'
DESCRIPTION = 'Astronomy Picture Of the Day'
URL = 'https://apod.nasa.gov/apod/astropix.html'


def pre_process(subkey):
    return None


def _process(url):
    soup = utils.get_soup_from_url(url)
    return utils.find_tags_from_soup(soup, "img")[0].parent.get('href')


def process(date, subkey):
    try:
        img = _process(URL)
    except Exception:
        try:
            print('Could not find today\'s picture, getting yesterday\'s one')
            date = date - datetime.timedelta(days=1)
            img = _process('https://apod.nasa.gov/apod/ap' + date.strftime("%y%m%d") + '.html')
        except Exception:
            raise WallmeException('No picture found today neither yesterday. It could be a video.')

    return 'https://apod.nasa.gov/apod/' + img


def post_process(image):
    return None
