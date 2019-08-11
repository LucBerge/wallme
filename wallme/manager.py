import requests, platform, os, ctypes
from datetime import date
from pathlib import Path
from wallme.websites import WEBSITES

class Manager():

	IMAGE = str(Path.home()) + '/wallme.jpg'

	def __init__(self, name):
		if(name not in WEBSITES.keys()):
			raise Exception("Website '" + name + "' not supported. Use the -l option to list all posibilities.")
		
		self.website = WEBSITES[name]

	def wallme(self):
		#Get website url
		today = date.today()
		webpageurl = self.website.getWebPageUrl((today.strftime("%d"), today.strftime("%m"), today.strftime("%Y")))

		#Retrieve webpage
		result = requests.get(webpageurl)
		if result.status_code != 200:
			raise Exception("Cannot retrieve webpage '" + webpageurl + "'. Please make sure the url is valid.")

		#Get picture url
		pictureurl = self.website.getPictureUrl(result.text)

		#Download image
		img_data = requests.get(pictureurl).content
		with open(self.IMAGE, 'wb') as handler:
			handler.write(img_data)

		#Set wallpaper
		self.setWallpaper(self.IMAGE)

#################
# SET WALLPAPER #
#################

	def setWallpaper(self, image):
		if not os.path.isfile(image):
			raise Exception("File '" + image + "' does not exists")

		image = os.path.abspath(image)
		system = platform.system()

		if(system == "Linux"):
			self.setWallpaperLinux(image)
		elif(system == "Windows"):
			self.setWallpaperWindows(image)
		else:
			raise Exception("Unknown system : '" + system + "'")

	def setWallpaperLinux(self, image):
		if os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri " + image) != 0:
			raise Exception("Cannot set wallpaper")

	def setWallpaperWindows(self, image): 
		if ctypes.windll.user32.SystemParametersInfoW(20, 0, image, 0) != 1:
			raise Exception("Cannot set wallpaper")