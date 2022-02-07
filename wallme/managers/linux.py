# coding: utf8

import os
from pathlib import Path
from .manager import Manager
from ..exceptions import WallmeException


class Linux(Manager):

    DATA_FOLDER = str(Path.home())
    SERVICE_FILE = "/lib/systemd/system/wallme.service"

    def __init__(self):
        super().__init__(self.DATA_FOLDER)

    def set(self, website, subkey, test=False):
        super().download(website, subkey, test)
        if(not test):
            if os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri " + self.IMAGE) != 0:
                raise WallmeException("Cannot set wallpaper")

    def set_startup(self, website, subkey):
        self.unset_startup()
        if subkey:
            fullkey = website.KEY + '.' + subkey
        else:
            fullkey = website.KEY
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
ExecStart=/usr/local/bin/wallme -set " + fullkey + "\n\
\n\
[Install]\n\
WantedBy=multi-user.target")
        os.system("sudo systemctl enable wallme")

    def unset_startup(self):
        if(os.path.exists(self.SERVICE_FILE)):
            os.remove(self.SERVICE_FILE)
            os.system("sudo systemctl disable wallme")
