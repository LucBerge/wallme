# coding: utf8

from .test_website import TestWebsite
from wallme.websites.astrobin import Astrobin


class TestAstrobin(TestWebsite):
    def test_apod(self):
        self.simple_test("astrobin", "astrobin", None, Astrobin)
