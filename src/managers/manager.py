# coding: utf8

import requests
from datetime import date
from pathlib import Path
import webbrowser
import os


class Manager():

    IMAGE = os.path.dirname(os.path.dirname(__file__)) + '\wallme.jpg'

    def download(self, website, subkey):
        # Pre process
        website.pre_process(subkey)
        # Get image url
        image_url = website.process(date.today(), subkey)
        # Download image
        img_data = requests.get(image_url).content
        with open(self.IMAGE, 'wb') as handler:
            handler.write(img_data)
        # Post process
        website.post_process(self.IMAGE)

    def info(self, website, subkey):
        # Pre process
        website.pre_process(date.today(), subkey)
        # Open the browser
        webbrowser.open(website.URL, new=2)

    def url(self, website, subkey):
        # Pre process
        website.pre_process(date.today(), subkey)
        # Get image url
        image_url = website.process(date.today(), subkey)
        # Print image url
        print(image_url)
