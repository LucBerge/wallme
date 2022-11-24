# coding: utf8

from .test_website import TestWebsite
from wallme.websites.national_geographic import NationalGeographic


class TestNationalGeographic(TestWebsite):
    def test_national_geographic(self):
        self.simple_test("national-geographic", "national-geographic", None, NationalGeographic)
