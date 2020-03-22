from wallme import utils

NAME = 'telegraph'
DESCRIPTION = 'The Telegraph picture of the day'

def pre_process():
	return None
    
def process(date):
	soup = utils.get_soup_from_url('https://www.telegraph.co.uk/news/pictures/')
	h3s = utils.find_tags_from_soup(soup, "h3", attributes={"class": "u-heading-6"})
	soup = utils.get_soup_from_url("https://www.telegraph.co.uk" + h3s[0].a.get('href'))
	imgs = utils.find_tags_from_soup(soup, "img", attributes={"class": "gallery__regwall-image"})
	return "https://www.telegraph.co.uk" + imgs[0].get('src').split('?')[0]

def post_process(image):
	return None