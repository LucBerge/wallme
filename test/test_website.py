# coding: utf8

from wallme import utils
from wallme.managers.managerfactory import ManagerFactory


class TestWebsite:

    def simple_test(self, full_key, expected_key, expected_subkey, expected_website, date=None):

        key, subkey = utils.get_key_subkey_from_fullkey(full_key)
        assert key == expected_key
        assert subkey == expected_subkey

        website = utils.get_website_from_key(key)
        assert type(website) == expected_website

        manager = ManagerFactory().get_manager()

        if (date is not None):
            manager.today = date

        manager.set(full_key, test=True)
