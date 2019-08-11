import re, json

NAME = 'bing'
DESCRIPTION = 'Bing daily wallpaper images gallery for several countries'

def getWebPageUrl(date):
	return 'http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=EN-IN'

def getPictureUrl(webpage):
	webpage_data = json.loads(webpage)
	return "https://www.bing.com" + webpage_data['images'][0]['url']