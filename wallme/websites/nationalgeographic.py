import json

NAME = 'national-geographic'
DESCRIPTION = 'One photo of the world every day'

def getWebPageUrl(date):
	return 'https://www.nationalgeographic.com/photography/photo-of-the-day/_jcr_content/.syndication-gallery.json'

def getPictureUrl(webpage):
	webpage_data = json.loads(webpage)
	renditions = webpage_data['items'][0]['renditions']
	sorted_renditions = sorted(renditions, key=lambda i:int(i['width']), reverse=True)
	return renditions[2]['uri']