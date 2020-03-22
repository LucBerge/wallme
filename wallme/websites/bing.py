from wallme import utils

NAME = 'bing'
DESCRIPTION = 'Bing daily wallpaper images gallery for several countries'

def pre_process():
	return None
    
def process(date):
	json = utils.get_json_from_url('http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=EN-IN')
	return "https://www.bing.com" + json['images'][0]['url']
    
def post_process(image):
	return None