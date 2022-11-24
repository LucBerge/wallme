# coding: utf8

from .website import Website


class Wikipedia(Website):
    key = 'wikipedia'
    description = 'English wikipedia picture of the day, mostly about history'
    domain = "https://en.wikipedia.org"
    url = domain + "/wiki/Wikipedia:Picture_of_the_day"

    def process(self, date, subkey):
        soup = self.get_soup_from_url(self.url)
        links = self.find_tags_from_soup(soup, "a", attributes={"class": "image"})
        soup = self.get_soup_from_url(self.domain + links[0].get('href'))
        divs = self.find_tags_from_soup(soup, "div", attributes={"class": "fullImageLink"})
        return "https:" + divs[0].a.get('href')
