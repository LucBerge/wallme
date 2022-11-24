# coding: utf8

from .test_website import TestWebsite
from wallme.websites.reddit import Reddit


class TestReddit(TestWebsite):

    def test_reddit_cityporn(self):
        self.simple_test("reddit.cityporn", "reddit", "cityporn", Reddit)

    def test_reddit_earthporn(self):
        self.simple_test("reddit.earthporn", "reddit", "earthporn", Reddit)

    def test_reddit_sexywomanoftheday(self):
        self.simple_test("reddit.sexywomanoftheday", "reddit", "sexywomanoftheday", Reddit)

    def test_reddit_error(self):
        try:
            self.simple_test("reddit", "reddit", None, Reddit)
            assert False
        except Exception:
            assert True

    def test_reddit_no_image(self):
        try:
            self.simple_test("reddit.askreddit", "reddit", "askreddit", Reddit)
            assert False
        except Exception:
            assert True
