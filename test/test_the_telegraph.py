# coding: utf8

from .test_website import TestWebsite
from wallme.websites import the_telegraph


class TestTheTelegraph(TestWebsite):
    def test_the_telegraph(self):
        self.simple_test("the-telegraph", "the-telegraph", None, the_telegraph)
