# coding: utf8

from .test_website import TestWebsite
from wallme.websites.bing import Bing


class TestBing(TestWebsite):
    def test_bing(self):
        self.simple_test("bing", "bing", None, Bing)
