# coding: utf8

from .website import Website


class TheTelegraph(Website):
    key = 'the-telegraph'
    description = 'Pictures reflecting the political, social or environmental situations in the world'
    info_url = 'https://www.telegraph.co.uk/pictures-of-the-day/'
    image_url = 'https://www.telegraph.co.uk'

    def process(self, date, subkey):
        soup = self.get_soup_from_url(self.info_url)
        h2s = self.find_tags_from_soup(soup, "h2", attributes={"class": "u-heading-1"})
        soup = self.get_soup_from_url("https://www.telegraph.co.uk" + h2s[0].a.get('href'))
        imgs = self.find_tags_from_soup(soup, "img", attributes={"class": "gallery-item__image"})
        return self.image_url + imgs[0].get('src').split('?')[0]
