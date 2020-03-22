from wallme import utils
from PIL import Image

NAME = 'astrobin'
DESCRIPTION = 'Pictures of Galaxies, Stars and Planets'

def pre_process():
    return None

def process(date):
	soup = utils.get_soup_from_url('https://www.astrobin.com/iotd/archive/')
	divs = utils.find_tags_from_soup(soup, "div", attributes={"class": "astrobin-image-container"})
	soup = utils.get_soup_from_url("https://www.astrobin.com/full" + divs[0].a.get('href') + "/0")
	imgs = utils.find_tags_from_soup(soup, "img", attributes={"class": "astrobin-image"})
	return imgs[0].get('src')

def post_process(image):
	with Image.open(image) as img:
		width, height = img.size
		if(width < height):
			img = img.transpose(Image.ROTATE_90)
			img.save(image)
	