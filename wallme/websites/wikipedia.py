# coding: utf8

from .website import Website


class Wikipedia(Website):
    key = 'wikipedia'
    description = 'English wikipedia picture of the day, mostly about history'
    info_url = 'https://en.wikipedia.org/wiki/Wikipedia:Picture_of_the_day'

    def process(self, date, subkey):
        soup = self.get_soup_from_url(self.info_url)
        imgs = self.find_tags_from_soup(soup, "img", attributes={"class": "mw-file-element"})
        thumb_image = imgs[0].get('src')
        file_name = thumb_image.split('px-')[-1]
        thumb_base = thumb_image.split(file_name)[0]
        return "https:" + thumb_base.replace('/thumb', '') + file_name

