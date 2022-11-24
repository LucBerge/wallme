# coding: utf8

from .website import Website


class NationalGeographic(Website):
    key = 'national-geographic'
    description = 'The National-Geographic magazine gives you pictures about live on earth'
    url = 'https://www.nationalgeographic.com/photo-of-the-day/'

    def process(self, date, subkey):
        soup = self.get_soup_from_url(self.url)
        images = self.find_tags_from_soup(soup, "meta", attributes={"property": "og:image"})
        return images[0].get('content')
