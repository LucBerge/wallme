# coding: utf8

from .test_website import TestWebsite
from wallme.websites.nasa import Nasa


class TestNasa(TestWebsite):
    def test_nasa(self):
        self.simple_test("nasa", "nasa", None, Nasa)
