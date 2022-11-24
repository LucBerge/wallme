# coding: utf8

from .test_website import TestWebsite
from wallme.websites.wikipedia import Wikipedia


class TestWikipedia(TestWebsite):
    def test_wikipedia(self):
        self.simple_test("wikipedia", "wikipedia", None, Wikipedia)
