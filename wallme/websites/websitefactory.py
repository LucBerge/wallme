from wallme.websites import WEBSITES
from wallme.exceptions import WallmeException

class WebsiteFactory():

	def get_website(self, name):
		if(name not in WEBSITES.keys()):
			raise WallmeException("Website '" + name + "' not supported. Use the -list option to list all posibilities.")
		
		return WEBSITES[name]