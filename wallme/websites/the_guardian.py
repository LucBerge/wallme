# coding: utf8

from .website import Website


class TheGuardian(Website):
    key = 'the-guardian'
    description = 'Each day the picture editor of the Guardian brings you a selection of photo highlights'
    url = 'https://www.theguardian.com/news/series/ten-best-photographs-of-the-day'

    def process(self, date, subkey):
        soup = self.get_soup_from_url(self.url)
        imgs = self.find_tags_from_soup(soup, "a", attributes={"class": "u-faux-block-link__overlay"})
        soup = self.get_soup_from_url(imgs[0].get('href'))
        sources = self.find_tags_from_soup(soup, "source", attributes={"sizes": "1900px"})
        return sources[0].get('srcset').split(' ')[0]
