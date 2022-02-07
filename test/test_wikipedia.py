# coding: utf8

from .test_website import TestWebsite
from wallme.websites import wikipedia


class TestWikipedia(TestWebsite):
    def test_wikipedia(self):
        self.simple_test("wikipedia", "wikipedia", None, wikipedia)
