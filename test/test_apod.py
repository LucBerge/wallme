# coding: utf8

from .test_website import TestWebsite
from wallme.websites import apod
import datetime


class TestApod(TestWebsite):
    def test_apod(self):
        self.simple_test("apod", "apod", None, apod)

    def test_apod_video(self):
        apod.URL = "https://apod.nasa.gov/apod/ap220209.html"
        date = datetime.datetime.strptime('09/02/2022', '%d/%m/%Y')
        self.simple_test("apod", "apod", None, apod, date=date)

    def test_apod_error(self):
        apod.URL = "https://fake.url"
        date = datetime.datetime.strptime('10/02/2022', '%d/%m/%Y')
        try:
            self.simple_test("apod", "apod", None, apod, date=date)
            assert False
        except Exception:
            assert True
