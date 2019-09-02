import re

NAME = 'wikipedia'
DESCRIPTION = 'English wikipedia picture of the day'

def getWebPageUrl(date):
	return 'https://en.wikipedia.org/wiki/Wikipedia:Picture_of_the_day'

def getPictureUrl(webpage):
	search = re.search(r'<img (.*?) src="(?P<uri>.*?)"',webpage)

	if(search == None):
		raise Exception("Unable to find the image.")

	return "http:" + search.group('uri').replace('399px', '1920px')
