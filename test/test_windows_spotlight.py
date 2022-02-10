# coding: utf8

from .test_website import TestWebsite
from wallme.websites import windows_spotlight


class TestWindowsSpotlight(TestWebsite):
    def test_wikipedia(self):
        self.simple_test("windows-spotlight", "windows-spotlight", None, windows_spotlight)
