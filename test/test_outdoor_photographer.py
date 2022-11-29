# coding: utf8

from .test_website import TestWebsite


class TestOutdoorPhotographer(TestWebsite):
    def test_info(self):
        self._test_info("outdoor-photographer")

    def test_url(self):
        self._test_url("outdoor-photographer")

    def test_set(self):
        self._test_set("outdoor-photographer")
