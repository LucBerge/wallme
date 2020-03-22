from wallme import utils

NAME = 'the-guardian'
DESCRIPTION = 'Each day the picture editor of the Guardian brings you a selection of photo highlights'

def pre_process():
	return None

def process(date):
	soup = utils.get_soup_from_url('https://www.theguardian.com/news/series/ten-best-photographs-of-the-day')
	imgs = utils.find_tags_from_soup(soup, "a", attributes={"class": "u-faux-block-link__overlay"})
	soup = utils.get_soup_from_url(imgs[0].get('href'))
	sources = utils.find_tags_from_soup(soup, "source", attributes={"sizes": "1900px"})
	return sources[0].get('srcset').split(' ')[0]
    
def post_process(image):
	return None