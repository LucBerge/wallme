# coding: utf8

from .website import Website


class Tetras(Website):
    key = 'tetras'
    description = 'Amateur pictures of the Alpes and the Dauphine'
    url = 'http://tetras.org/Semaine.jpg'

    def process(self, date, subkey):
        return self.url
