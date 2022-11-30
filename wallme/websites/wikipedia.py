# coding: utf8

from .website import Website


class Wikipedia(Website):
    key = 'wikipedia'
    description = 'English wikipedia picture of the day, mostly about history'
    info_url = 'https://en.wikipedia.org/wiki/Wikipedia:Picture_of_the_day'
    process_url = "https://en.wikipedia.org"

    def process(self, date, subkey):
        soup = self.get_soup_from_url(self.info_url)
        links = self.find_tags_from_soup(soup, "a", attributes={"class": "image"})
        soup = self.get_soup_from_url(self.process_url + links[0].get('href'))
        divs = self.find_tags_from_soup(soup, "div", attributes={"class": "fullImageLink"})
        return "https:" + divs[0].a.get('href')
