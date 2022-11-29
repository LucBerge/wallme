# coding: utf8

from .test_website import TestWebsite


class TestBing(TestWebsite):
    def test_info(self):
        self._test_info("bing")

    def test_url(self):
        self._test_url("bing")

    def test_set(self):
        self._test_set("bing")

    def test_set_unset_startup(self):
        self._test_set_unset_startup("bing")
