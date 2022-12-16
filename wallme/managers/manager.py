# coding: utf8

import requests
import webbrowser
import os
import datetime
from ..log import logger
from .. import utils


class Manager():

    BACKGROUND_IMAGE_NAME = "background.jpg"
    GUI_IMAGE_NAME = "gui.jpg"
    PRANK_KEY = "reddit.sexywomanoftheday"

    def __init__(self, entry_point, data_folder):
        if('.py' in entry_point):
            entry_point = 'wallme'
        self.entry_point = entry_point
        if (not os.path.isdir(data_folder)):
            os.makedirs(data_folder, 493)
        self.background_image = os.path.join(data_folder, self.BACKGROUND_IMAGE_NAME)
        self.gui_image = os.path.join(data_folder, self.GUI_IMAGE_NAME)
        self.today = datetime.date.today()

    def download(self, full_key, gui, test=False):
        # Parse full key
        website, subkey = utils.get_website_subkey_from_fullkey(full_key)
        # Pre process
        website.pre_process(subkey)
        # Get image url
        image_url = website.process(self.today, subkey)
        # Download image
        logger.debug("Downloading image from " + image_url, flush=True)
        img_data = requests.get(image_url, headers=website.HEADERS).content
        # Choose the image path
        if(gui):
            image_path = self.gui_image
        else:
            image_path = self.background_image
        # Save the image file
        with open(image_path, 'wb') as handler:
            handler.write(img_data)
        logger.debug("Image saved to " + image_path)
        # Post process
        website.post_process(image_path)
        #Return the image path
        return image_path

    def info(self, full_key, test=False):
        # Parse full key
        website, subkey = utils.get_website_subkey_from_fullkey(full_key)
        # Pre process
        website.pre_process(subkey)
        # Open the browser
        if (not test):
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
