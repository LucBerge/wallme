# coding: utf8

from .test_website import TestWebsite


class TestWindowsSpotlight(TestWebsite):
    def test_info(self):
        self._test_info("windows-spotlight")

    def test_url(self):
        self._test_url("windows-spotlight")

    def test_set(self):
        self._test_set("windows-spotlight")

    def test_set_unset_startup(self):
        self._test_set_unset_startup("windows-spotlight")
