# coding: utf8

from .test_website import TestWebsite
from wallme.websites.the_guardian import TheGuardian


class TestTheGuardian(TestWebsite):
    def test_the_guardian(self):
        self.simple_test("the-guardian", "the-guardian", None, TheGuardian)
