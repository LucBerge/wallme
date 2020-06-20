from wallme import utils

NAME = 'epod'
DESCRIPTION = 'Earth Picture of the Day'
URL = 'https://epod.usra.edu/'

def pre_process():
	return None

def process(date):
	soup = utils.get_soup_from_url(URL)
	imgs = utils.find_tags_from_soup(soup, "a", attributes={"class": "asset-img-link"})
	return imgs[0].get('href')
    
def post_process(image):
	return None