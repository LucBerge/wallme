from .. import utils
from ..exceptions import WallmeException

KEY = 'reddit'
TEST_KEY = 'reddit.earthporn'
DESCRIPTION = 'Top pictures from the topic of your choice. Use reddit.<topic> as the key. (e.g. : reddit.earthporn)'
URL = 'http://www.reddit.com/r/'

def pre_process():
    global URL
    try:
    	URL = URL + subkey
    except:
    	raise WallmeException("Missing subkey : Please use 'reddit.<subkey>'.")
    return None
    
def process(date):
    json = utils.get_json_from_url('http://www.reddit.com/r/' + subkey + '/top/.json?limit=100')
    
    for children in json['data']['children']:
        if("i.redd.it" in children['data']['url']):
            return children['data']['url']
    
    raise WallmeException("No image found today...")
    
def post_process(image):
    return None