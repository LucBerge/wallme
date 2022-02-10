# coding: utf8

from .test_website import TestWebsite
from wallme.websites import reddit


class TestReddit(TestWebsite):

    def test_reddit_cityporn(self):
        self.simple_test("reddit.cityporn", "reddit", "cityporn", reddit)

    def test_reddit_earthporn(self):
        self.simple_test("reddit.earthporn", "reddit", "earthporn", reddit)

    def test_reddit_sexywomanoftheday(self):
        self.simple_test("reddit.sexywomanoftheday", "reddit", "sexywomanoftheday", reddit)

    def test_reddit_error(self):
        try:
            self.simple_test("reddit", "reddit", None, reddit)
            assert False
        except Exception:
            assert True

    def test_reddit_no_image(self):
        reddit.URL = "https://fake.url"
        try:
            self.simple_test("reddit.cityporn", "reddit", "cityporn", reddit)
            assert False
        except Exception:
            assert True
