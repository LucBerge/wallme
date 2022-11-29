# coding: utf8

from .test_website import TestWebsite
from wallme.websites.apod import Apod
import datetime


class TestApod(TestWebsite):
    def test_info(self):
        self._test_info("apod")

    def test_url(self):
        self._test_url("apod")

    def test_set(self):
        self._test_set("apod")

    def test_set_video(self):
        Apod.url = "https://apod.nasa.gov/apod/ap220209.html"
        date = datetime.datetime.strptime('09/02/2022', '%d/%m/%Y')
        self._test_set("apod", date=date)

    def test_set_error(self):
        Apod.url = "https://fake.url"
        date = datetime.datetime.strptime('10/02/2022', '%d/%m/%Y')
        try:
            self._test_set("apod", date=date)
            assert False
        except Exception:
            assert True
