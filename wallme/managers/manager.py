# coding: utf8

import requests
import webbrowser
import os
from datetime import date
from pathlib import Path


class Manager():
    
    def __init__(self, data_folder):
        if(not os.path.isdir(data_folder)):
            os.makedirs(data_folder, 493)
        self.image =  data_folder + '\wallme.jpg'

    def download(self, website, subkey):
        # Pre process
        website.pre_process(subkey)
        # Get image url
        image_url = website.process(date.today(), subkey)
        # Download image
        img_data = requests.get(image_url).content
        with open(self.image, 'wb') as handler:
            handler.write(img_data)
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
        image_url = website.process(date.today(), subkey)
        # Print image url
        print(image_url)
