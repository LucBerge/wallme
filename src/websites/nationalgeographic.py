from .. import utils

KEY = 'national-geographic'
TEST_KEY = KEY
DESCRIPTION = 'The magazin National-Geographic magazine gives you pictures about live on earth'
URL = 'https://www.nationalgeographic.com/photography/photo-of-the-day'

def pre_process():
	return None

def process(date):
	json = utils.get_json_from_url('https://www.nationalgeographic.com/photography/photo-of-the-day/_jcr_content/.syndication-gallery.json')
	renditions = json['items'][0]['image']['renditions']
	sorted_renditions = sorted(renditions, key=lambda i:int(i['width']), reverse=True)
	return sorted_renditions[0]['uri']

def post_process(image):
	return None