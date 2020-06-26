from . import WEBSITES
from ..exceptions import WallmeException

class WebsiteFactory():

    def get_website(self, key):
    
        dot_index = key.find('.')
        if dot_index > 0:
            subkey = key[dot_index+1:]
            key = key[:dot_index]
    
        if(key not in WEBSITES.keys()):
            raise WallmeException("Website '" + key + "' not supported. Use the -list option to list all the posibilities.")
        
        if(dot_index > 0):
            WEBSITES[key].subkey = subkey
            
        return WEBSITES[key]