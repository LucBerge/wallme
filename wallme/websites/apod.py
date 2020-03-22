from wallme import utils
from wallme.exceptions import ProcessException

NAME = 'apod'
DESCRIPTION = 'Astronomy Picture of the Day'

def pre_process():
	return None
    
def process(date):
    try:
        soup = utils.get_soup_from_url('https://apod.nasa.gov/apod/astropix.html')
        imgs = utils.find_tags_from_soup(soup, "img")
        return 'https://apod.nasa.gov/apod/' + imgs[0].get('src')
    except:
        raise ProcessException('No picture found today. It could be a video.') 
    
def post_process(image):
	return None