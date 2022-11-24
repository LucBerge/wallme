# coding: utf8

from .website import Website


class Epod(Website):
    key = 'epod'
    description = 'Earth Picture Of the Day'
    url = 'https://epod.usra.edu/'


    def process(self, date, subkey):
        soup = self.get_soup_from_url(self.url)
        imgs = self.find_tags_from_soup(soup, "a", attributes={"class": "asset-img-link"})
        return imgs[0].get('href')
