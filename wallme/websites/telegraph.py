import re

NAME = 'telegraph'
DESCRIPTION = 'The Telegraph picture of the day'

def getWebPageUrl(date):
	month = date.strftime('%B').lower()
	return date.strftime("https://www.telegraph.co.uk/news/%Y/%m/%d/pictures-day-%-d-" + month + "-%Y/")

def getPictureUrl(webpage):
	pictureurl = re.search(r'<img class="responsive gallery__regwall-image" src="(.*?)\?',webpage)
	
	if(pictureurl == None):
		raise Exception("Unable to find the image.")

	return 'https://www.telegraph.co.uk' + pictureurl.group(1)