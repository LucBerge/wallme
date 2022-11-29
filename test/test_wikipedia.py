# coding: utf8

from .test_website import TestWebsite


class TestWikipedia(TestWebsite):
    def test_info(self):
        self._test_info("wikipedia")

    def test_url(self):
        self._test_url("wikipedia")

    def test_set(self):
        self._test_set("wikipedia")

    def test_set_unset_startup(self):
        self._test_set_unset_startup("wikipedia")
