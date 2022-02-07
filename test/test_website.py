# coding: utf8

from wallme import utils
from wallme.managers.managerfactory import ManagerFactory
from wallme.websites.websitefactory import WebsiteFactory


class TestWebsite:

    def simple_test(self, full_key, expected_key, expected_subkey, expected_website):

        key, subkey = utils.get_key_subkey_from_fullkey(full_key)
        assert key == expected_key
        assert subkey == expected_subkey

        website = WebsiteFactory().get_website(key)
        assert website == expected_website

        manager = ManagerFactory().get_manager()
        manager.set(website, subkey, test=True)
