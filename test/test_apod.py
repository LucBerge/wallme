# coding: utf8

from .test_website import TestWebsite
from wallme.websites import apod


class TestApod(TestWebsite):
    def test_apod(self):
        self.simple_test("apod", "apod", None, apod)
