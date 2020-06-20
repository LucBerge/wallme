import os
from wallme.managers.manager import Manager
from wallme.exceptions import WallmeException

class Linux(Manager):
        
	SERVICE_FILE = "/lib/systemd/system/wallme.service"

	def set(self, website, test=False):
		super().download(website)
		if(not test):
			if os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri " + self.IMAGE) != 0:
				raise WallmeException("Cannot set wallpaper")
            
	def set_startup(self, website):
		
		self.unset_startup()
        
		user = os.popen("who | awk 'FNR == 1 {print $1}'").read().rstrip()
		
		if(not os.path.exists(self.SERVICE_FILE)):
			with open(self.SERVICE_FILE, "wt") as f:
				f.write("[Unit]\n\
Description=Wallme service.\n\
After=network-online.target\n\
\n\
[Service]\n\
Type=simple\n\
User=" + user + "\n\
Group=" + user + "\n\
ExecStart=/usr/local/bin/wallme -set " + website.NAME + "\n\
\n\
[Install]\n\
WantedBy=multi-user.target")

		os.system("sudo systemctl enable wallme")

	def unset_startup(self):
		if(os.path.exists(self.SERVICE_FILE)):
			os.remove(self.SERVICE_FILE)
			os.system("sudo systemctl disable wallme")