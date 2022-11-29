# coding: utf8

from .test_website import TestWebsite


class TestTheGuardian(TestWebsite):
    def test_info(self):
        self._test_info("the-guardian")

    def test_url(self):
        self._test_url("the-guardian")

    def test_set(self):
        self._test_set("the-guardian")

    def test_set_unset_startup(self):
        self._test_set_unset_startup("the-guardian")
