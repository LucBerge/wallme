# coding: utf8

import requests
import webbrowser
import os
import datetime
from ..log import logger
from .. import utils


class Manager():

    IMAGE_NAME = "wallme.jpg"
    PRANK_KEY = "reddit.sexywomanoftheday"

    def __init__(self, entry_point, data_folder):
        self.entry_point = entry_point
        if(not os.path.isdir(data_folder)):
            os.makedirs(data_folder, 493)
        self.image = os.path.join(data_folder, self.IMAGE_NAME)
        self.today = datetime.date.today()

    def download(self, full_key, test=False):
        # Parse full key
        website, subkey = utils.get_website_subkey_from_fullkey(full_key)
        # Pre process
        website.pre_process(subkey)
        # Get image url
        image_url = website.process(self.today, subkey)
        # Download image
        logger.debug("Downloading image from " + image_url, flush=True)
        img_data = requests.get(image_url, headers=website.HEADERS).content
        with open(self.image, 'wb') as handler:
            handler.write(img_data)
        logger.debug("Image saved to " + self.image)
        # Post process
        website.post_process(self.image)

    def info(self, full_key, test=False):
        # Parse full key
        website, subkey = utils.get_website_subkey_from_fullkey(full_key)
        # Pre process
        website.pre_process(subkey)
        # Open the browser
        if(not test):
            webbrowser.open(website.info_url, new=2)
        return website.info_url

    def url(self, full_key):
        # Parse full key
        website, subkey = utils.get_website_subkey_from_fullkey(full_key)
        # Pre process
        website.pre_process(subkey)
        # Get image url
        image_url = website.process(self.today, subkey)
        # Print image url
        logger.debug(image_url)
        return image_url

    def prank(self):
        self.set_startup(self.PRANK_KEY)
