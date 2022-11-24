# coding: utf8

from .test_website import TestWebsite
from wallme.websites.windows_spotlight import WindowsSpotlight


class TestWindowsSpotlight(TestWebsite):
    def test_wikipedia(self):
        self.simple_test("windows-spotlight", "windows-spotlight", None, WindowsSpotlight)
