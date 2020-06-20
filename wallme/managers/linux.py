import os
from wallme.managers.manager import Manager
from wallme.exceptions import WallmeException

class Linux(Manager):
        
	def set(self, website):
		super().download(website)
		if(not test):
			if os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri " + self.IMAGE) != 0:
				raise WallmeException("Cannot set wallpaper")
            
	def set_startup(self, website):
		#Get the starup folder
		#Create a bat file
		#Fill the bat file
		pass

	def unset_startup(self): 
		#Get the starup folder
		#Remove the bat file
		pass