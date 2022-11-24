# coding: utf8

from .website import Website


class TheTelegraph(Website):
    key = 'the-telegraph'
    description = 'Pictures reflecting the political, social or environmental situations in the world'
    domain = 'https://www.telegraph.co.uk'
    url = domain + '/pictures-of-the-day/'


    def process(self, date, subkey):
        soup = self.get_soup_from_url(self.url)
        h2s = self.find_tags_from_soup(soup, "h2", attributes={"class": "u-heading-1"})
        soup = self.get_soup_from_url("https://www.telegraph.co.uk" + h2s[0].a.get('href'))
        imgs = self.find_tags_from_soup(soup, "img", attributes={"class": "gallery-item__image"})
        return self.domain + imgs[0].get('src').split('?')[0]
