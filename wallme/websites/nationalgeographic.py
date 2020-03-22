from wallme import utils

NAME = 'national-geographic'
DESCRIPTION = 'One photo of the world every day'

def pre_process():
	return None

def process(date):
	json = utils.get_json_from_url('https://www.nationalgeographic.com/photography/photo-of-the-day/_jcr_content/.syndication-gallery.json')
	renditions = json['items'][0]['image']['renditions']
	sorted_renditions = sorted(renditions, key=lambda i:int(i['width']), reverse=True)
	return sorted_renditions[0]['uri']

def post_process(image):
	return None