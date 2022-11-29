# coding: utf8

from .test_website import TestWebsite


class TestTetras(TestWebsite):
    def test_info(self):
        self._test_info("tetras")

    def test_url(self):
        self._test_url("tetras")

    def test_set(self):
        self._test_set("tetras")
