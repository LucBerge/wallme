from .. import utils
from ..exceptions import WallmeException

KEY = 'apod'
TEST_KEY = KEY
DESCRIPTION = 'Astronomy Picture Of the Day'
URL = 'https://apod.nasa.gov/apod/astropix.html'

def pre_process():
	return None
    
def process(date):
    try:
        soup = utils.get_soup_from_url(URL)
        imgs = utils.find_tags_from_soup(soup, "img")
        return 'https://apod.nasa.gov/apod/' + imgs[0].get('src')
    except:
        raise WallmeException('No picture found today. It could be a video.') 
    
def post_process(image):
	return None