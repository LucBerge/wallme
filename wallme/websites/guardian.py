import re, requests

NAME = 'guardian'
DESCRIPTION = 'Each day the picture editor of the Guardian brings you a selection of photo highlights'

def getWebPageUrl(date):
	return "https://www.theguardian.com/news/series/ten-best-photographs-of-the-day"

def getPictureUrl(webpage):
	
	pageurl = re.search(r'<a href="(.*?)" class="u-faux-block-link__overlay js-headline-text"',webpage)

	if(pageurl == None):
		raise Exception("Unable to find the image.")

	webpage = requests.get(pageurl.group(1)).text
	pictureurl = re.search(r'sizes="1900px" srcset="(.*?)"', webpage)

	if(pictureurl == None):
		raise Exception("Unable to find the image.")

	space_index = pictureurl.group(1).find(' ')

	return pictureurl.group(1)[:space_index].replace('amp;','')