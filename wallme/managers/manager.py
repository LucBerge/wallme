# coding: utf8

import requests
import webbrowser
import os
import datetime
from ..log import logger


class Manager():

    IMAGE_NAME = "wallme.jpg"

    def __init__(self, data_folder):
        if(not os.path.isdir(data_folder)):
            os.makedirs(data_folder, 493)
        self.image = os.path.join(data_folder, self.IMAGE_NAME)

    def download(self, website, subkey, test=False):
        # Pre process
        website.pre_process(subkey)
        # Get image url
        image_url = website.process(datetime.date.today(), subkey)
        # Download image
        logger.debug("Downloading image from " + image_url, flush=True)
        img_data = requests.get(image_url).content
        with open(self.image, 'wb') as handler:
            handler.write(img_data)
        logger.debug("Image saved to " + self.image)
        # Post process
        website.post_process(self.image)

    def info(self, website, subkey):
        # Pre process
        website.pre_process(subkey)
        # Open the browser
        webbrowser.open(website.URL, new=2)

    def url(self, website, subkey):
        # Pre process
        website.pre_process(subkey)
        # Get image url
        image_url = website.process(datetime.date.today(), subkey)
        # Print image url
        logger.debug(image_url)
