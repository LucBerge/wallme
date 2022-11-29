# coding: utf8

from .test_website import TestWebsite


class TestNationalGeographic(TestWebsite):
    def test_info(self):
        self._test_info("national-geographic")

    def test_url(self):
        self._test_url("national-geographic")

    def test_set(self):
        self._test_set("national-geographic")
