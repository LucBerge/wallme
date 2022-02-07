# coding: utf8

from .test_website import TestWebsite
from wallme.websites import tetras


class TestTetras(TestWebsite):
    def test_tetras(self):
        self.simple_test("tetras", "tetras", None, tetras)
