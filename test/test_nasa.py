# coding: utf8

from .test_website import TestWebsite


class TestNasa(TestWebsite):
    def test_info(self):
        self._test_info("nasa")

    def test_url(self):
        self._test_url("nasa")

    def test_set(self):
        self._test_set("nasa")
