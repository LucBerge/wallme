import ctypes, os
from wallme.managers.manager import Manager
from wallme.exceptions import WallmeException

class Windows(Manager):

	STARTUP_FOLDER = os.path.expandvars(r'%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup')
	STARTUP_FILE = STARTUP_FOLDER + "\\wallme.bat"

	def set(self, website, test=False):
		super().download(website)
		if(not test):
			if ctypes.windll.user32.SystemParametersInfoW(20, 0, self.IMAGE, 3) != 1:
				raise WallmeException("Cannot set wallpaper")

	def set_startup(self, website):
		if(not os.path.exists(self.STARTUP_FOLDER)):
			os.makedirs(STARTUP_FOLDER)
		
		self.unset_startup()
        
		if(not os.path.exists(self.STARTUP_FILE)):
			with open(self.STARTUP_FILE, "wt") as f:
				f.write("wallme -set " + website.NAME)

	def unset_startup(self):
		if(os.path.exists(self.STARTUP_FILE)):
			os.remove(self.STARTUP_FILE)