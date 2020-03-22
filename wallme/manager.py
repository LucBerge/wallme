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

	def wallme(self, test=False):
		#Get image url
		pre_process_result = self.website.pre_process()
        
		#Get image url
		image_url = self.website.process(date.today())

		#Download image
		img_data = requests.get(image_url).content
		with open(self.IMAGE, 'wb') as handler:
			handler.write(img_data)

        #Flip image if necessary
		post_process_result = self.website.post_process(self.IMAGE)

		#Set wallpaper
		if(not test):
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
		if ctypes.windll.user32.SystemParametersInfoW(20, 0, image, 3) != 1:
			raise Exception("Cannot set wallpaper")