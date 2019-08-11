import re

NAME = 'apod'
DESCRIPTION = 'Astronomy Picture of the Day'

def getWebPageUrl(date):
	return 'https://apod.nasa.gov/apod/astropix.html'

def getPictureUrl(webpage):
	pictureurl = re.search("""<IMG SRC="(.*?)"[^>]*?>""",webpage)
    
	if(pictureurl == None):
		raise Exception("No image found today. It could be a video.")
    
	return 'https://apod.nasa.gov/apod/' + pictureurl.group(1)