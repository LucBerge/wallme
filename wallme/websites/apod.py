# coding: utf8

from .website import Website
from ..exceptions import WallmeException
import datetime
from ..log import logger


class Apod(Website):
    key = 'apod'
    description = 'Astronomy Picture Of the Day'
    info_url = 'https://apod.nasa.gov/apod/astropix.html'
    process_url = 'https://apod.nasa.gov/apod/ap'
    image_url = 'https://apod.nasa.gov/apod/'

    def _process(self, url):
        soup = self.get_soup_from_url(url)
        return self.find_tags_from_soup(soup, "img")[0].parent.get('href')

    def process(self, date, subkey):
        try:
            img = self._process(self.info_url)
        except Exception:
            try:
                logger.warning('Could not find today\'s picture, getting yesterday\'s one')
                date = date - datetime.timedelta(days=1)
                img = self._process(self.process_url + date.strftime("%y%m%d") + '.html')
            except Exception:
                raise WallmeException('No picture found today neither yesterday. It could be a video.')

        return self.image_url + img
