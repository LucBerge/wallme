from wallme import utils

NAME = 'nasa'
DESCRIPTION = 'NASA Image of the day'

def pre_process():
	return None

def process(date):
	json = utils.get_json_from_url('https://www.nasa.gov/api/2/ubernode/_search?size=1&from=0&sort=promo-date-time%3Adesc&q=((ubernode-type%3Aimage)%20AND%20(routes%3A1446))&_source_include=promo-date-time%2Cmaster-image%2Cnid%2Ctitle%2Ctopics%2Cmissions%2Ccollections%2Cother-tags%2Cubernode-type%2Cprimary-tag%2Csecondary-tag%2Ccardfeed-title%2Ctype%2Ccollection-asset-link%2Clink-or-attachment%2Cpr-leader-sentence%2Cimage-feature-caption%2Cattachments%2Curi')
	uri = json['hits']['hits'][0]['_source']['master-image']['uri']
	return "https://www.nasa.gov/sites/default/files/styles/full_width_feature/public/" + uri.replace("public://","")

def post_process(image):
	return None