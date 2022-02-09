# coding: utf8

from .test_website import TestWebsite
from wallme.websites import outdoor_photographer


class TestNasa(TestWebsite):
    def test_nasa(self):
        self.simple_test("outdoor-photographer", "outdoor-photographer", None, outdoor_photographer)
