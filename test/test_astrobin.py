# coding: utf8

from .test_website import TestWebsite


class TestAstrobin(TestWebsite):
    def test_info(self):
        self._test_info("astrobin")

    def test_url(self):
        self._test_url("astrobin")

    def test_set(self):
        self._test_set("astrobin")

    def test_set_unset_startup(self):
        self._test_set_unset_startup("astrobin")
