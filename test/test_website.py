# coding: utf8

from wallme.managers.managerfactory import ManagerFactory
import requests


class TestWebsite:
    HEADERS = {'User-Agent': 'Wallme-Bot/1.0'}

    def _test_info(self, full_key):
        manager = ManagerFactory().get_manager()
        url = manager.info(full_key, test=True)
        webpage = requests.get(url, headers=self.HEADERS)

        # Check status code
        assert webpage.status_code == 200

    def _test_url(self, full_key):
        manager = ManagerFactory().get_manager()
        url = manager.url(full_key)
        webpage = requests.get(url, headers=self.HEADERS)

        # Check status code
        assert webpage.status_code == 200
        # Check content type is an image
        assert 'image' in webpage.headers["Content-Type"]

    def _test_set(self, full_key, date=None):
        manager = ManagerFactory().get_manager()
        if (date is not None):
            manager.today = date
        manager.set(full_key, test=True)
