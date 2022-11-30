# coding: utf8

from .website import Website


class Bing(Website):
    key = 'bing'
    description = 'Various landscapes taken from the web search engine Bing'
    info_url = 'http://www.bing.com'
    process_url = info_url + '/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=EN-IN'

    def process(self, date, subkey):
        json = self.get_json_from_url(self.process_url)
        return self.info_url + json['images'][0]['url']
