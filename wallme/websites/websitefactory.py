# coding: utf8

from . import WEBSITES
from ..exceptions import WallmeException


class WebsiteFactory():

    def get_website(self, key):
        if(key not in WEBSITES.keys()):
            raise WallmeException("Website '" + key + "' not supported. Use the -list option to list all the posibilities.")
        return WEBSITES[key]
