# coding: utf8

from .test_website import TestWebsite
from wallme.websites import national_geographic


class TestNationalGeographic(TestWebsite):
    def test_national_geographic(self):
        self.simple_test("national-geographic", "national-geographic", None, national_geographic)
