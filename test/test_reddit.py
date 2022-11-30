# coding: utf8

from .test_website import TestWebsite


class TestReddit(TestWebsite):
    def test_info_cityporn(self):
        self._test_info("reddit.cityporn")

    def test_url_cityporn(self):
        self._test_url("reddit.cityporn")

    def test_set_cityporn(self):
        self._test_set("reddit.cityporn")

    def test_set_earthporn(self):
        self._test_set("reddit.earthporn")

    def test_set_sexywomanoftheday(self):
        self._test_set("reddit.sexywomanoftheday")

    def test_set_error(self):
        try:
            self._test_set("reddit")
            assert False
        except Exception:
            assert True

    def test_set_no_image(self):
        try:
            self._test_set("reddit.askreddit")
            assert False
        except Exception:
            assert True

    def test_set_unset_startup_cityporn(self):
        self._test_set_unset_startup("reddit.cityporn")
