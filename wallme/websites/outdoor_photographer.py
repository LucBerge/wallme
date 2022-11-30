# coding: utf8

from .website import Website


class OutdoorPhotographer(Website):
    key = 'outdoor-photographer'
    description = 'Outdoor pictures, essentially animals and landscapes'
    info_url = 'https://www.outdoorphotographer.com/blog/category/photo-of-the-day/'

    def process(self, date, subkey):
        soup = self.get_soup_from_url(self.info_url)
        imgs = self.find_tags_from_soup(soup, "img", attributes={"class": "wp-post-image"})
        links = imgs[0].get('srcset')
        return links.split(', ')[-1].split(' ')[-2]
