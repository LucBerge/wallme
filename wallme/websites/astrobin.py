# coding: utf8

from .website import Website
from PIL import Image

class Astrobin(Website):
    key = 'astrobin'
    description = 'Pictures of galaxies, stars and planets'
    url = 'https://www.astrobin.com/iotd/archive/'


    def process(self, date, subkey):
        soup = self.get_soup_from_url(self.url)
        divs = self.find_tags_from_soup(soup, "div", attributes={"class": "astrobin-image-container"})
        soup = self.get_soup_from_url("https://www.astrobin.com/full" + divs[0].a.get('href'))
        imgs = self.find_tags_from_soup(soup, "img", attributes={"class": "astrobin-image"})
        return imgs[0].get('src')


    def post_process(self, image):
        with Image.open(image) as img:
            width, height = img.size
            if(width < height):
                img = img.transpose(Image.ROTATE_90)
                img.save(image)
