import re

NAME = 'epod'
DESCRIPTION = 'Earth Picture of the Day'

def getWebPageUrl(date):
	return 'https://epod.usra.edu/'

def getPictureUrl(webpage):
	pictureurl = re.search(r'<a class="asset-img-link" href="(.*?)"',webpage)

	if(pictureurl == None):
		raise Exception("Unable to find the image.")
	
	return pictureurl.group(1)