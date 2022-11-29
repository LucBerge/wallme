# coding: utf8

from .test_website import TestWebsite


class TestEpod(TestWebsite):
    def test_info(self):
        self._test_info("epod")

    def test_url(self):
        self._test_url("epod")

    def test_set(self):
        self._test_set("epod")
