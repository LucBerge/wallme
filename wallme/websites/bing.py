# coding: utf8

from .website import Website


class Bing(Website):
    key = 'bing'
    description = 'Various landscapes taken from the web search engine Bing'
    url = 'http://www.bing.com'

    def process(self, date, subkey):
        json = self.get_json_from_url('http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=EN-IN')
        return "https://www.bing.com" + json['images'][0]['url']
