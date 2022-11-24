# coding: utf8

from .test_website import TestWebsite
from wallme.websites.epod import Epod


class TestEpod(TestWebsite):
    def test_epod(self):
        self.simple_test("epod", "epod", None, Epod)
