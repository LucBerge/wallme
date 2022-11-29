# coding: utf8

from .test_website import TestWebsite


class TestTheTelegraph(TestWebsite):
    def test_info(self):
        self._test_info("the-telegraph")

    def test_url(self):
        self._test_url("the-telegraph")

    def test_set(self):
        self._test_set("the-telegraph")
