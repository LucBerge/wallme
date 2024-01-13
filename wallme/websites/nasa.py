# coding: utf8

from .website import Website


class Nasa(Website):
    key = 'nasa'
    description = 'Pictures related to Nasa\'s missions'
    info_url = 'https://www.nasa.gov/image-of-the-day/'

    def process(self, date, subkey):
        soup = self.get_soup_from_url(self.info_url)
        images = self.find_tags_from_soup(soup, "img", attributes={"loading": "lazy"})
        return images[0].get('src')
