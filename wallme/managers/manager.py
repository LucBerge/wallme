# coding: utf8

import requests
import webbrowser
import os
import datetime


class Manager():

    def __init__(self, data_folder):
        if(not os.path.isdir(data_folder)):
            os.makedirs(data_folder, 493)
        self.image = data_folder + '\\wallme.jpg'

    def download(self, website, subkey, test=False):
        # Pre process
        website.pre_process(subkey)
        # Get image url
        image_url = website.process(datetime.date.today(), subkey)
        # Download image
        print("Downloading image from " + image_url, flush=True)
        img_data = requests.get(image_url).content
        # Stop here if it is a test
        if (test):
            return
        with open(self.image, 'wb') as handler:
            handler.write(img_data)
        print("Image saved to " + self.image)
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
        print(image_url)
