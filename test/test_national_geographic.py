# coding: utf8

from .test_website import TestWebsite
from wallme.websites import nationalgeographic


class TestNationalGeographic(TestWebsite):
    def test_national_geographic(self):
        self.simple_test("national-geographic", "national-geographic", None, nationalgeographic)
