from wallme import utils

NAME = 'wikipedia'
DESCRIPTION = 'English wikipedia picture of the day'

def pre_process():
	return None

def process(date):
	soup = utils.get_soup_from_url('https://en.wikipedia.org/wiki/Wikipedia:Picture_of_the_day')
	imgs = utils.find_tags_from_soup(soup, "img")
	current_width = imgs[0].get('width')
	full_width = imgs[0].get('data-file-width')
	return "https:" + imgs[0].get('src').replace(str(current_width + "px"), str(full_width + "px"))
    
def post_process(image):
	return None