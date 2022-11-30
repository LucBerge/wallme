# coding: utf8

from .website import Website


class WindowsSpotlight(Website):
    key = 'windows-spotlight'
    description = 'High resolution quality images from Windows 10 Spotlight'
    info_url = 'https://windows10spotlight.com/'

    def process(self, date, subkey):
        soup = self.get_soup_from_url(self.info_url)
        imgs = self.find_tags_from_soup(soup, "img", attributes={"class": "thumbnail wp-post-image"})
        links = imgs[0].get('srcset')
        return links.split(', ')[-1].split(' ')[-2]
