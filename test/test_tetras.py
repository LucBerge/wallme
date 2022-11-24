# coding: utf8

from .test_website import TestWebsite
from wallme.websites.tetras import Tetras


class TestTetras(TestWebsite):
    def test_tetras(self):
        self.simple_test("tetras", "tetras", None, Tetras)
