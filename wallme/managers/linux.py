# coding: utf8

import os
from pathlib import Path
from .manager import Manager
from ..exceptions import WallmeException


class Linux(Manager):

    DATA_FOLDER = str(Path.home()) + "/wallme"
    SERVICE_FILE = "/lib/systemd/system/wallme.service"

    def __init__(self, entry_point):
        super().__init__(entry_point, self.DATA_FOLDER)

    def set(self, full_key, test=False):
        super().download(full_key, test)
        if(not test):
            if os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri " + self.image) != 0:
                raise WallmeException("Cannot set wallpaper")

    def set_startup(self, full_key):
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
ExecStart=/usr/local/bin/wallme -set " + full_key + "\n\
\n\
[Install]\n\
WantedBy=multi-user.target")
        os.system("sudo systemctl enable wallme")

    def unset_startup(self):
        if(os.path.exists(self.SERVICE_FILE)):
            os.remove(self.SERVICE_FILE)
            os.system("sudo systemctl disable wallme")

    def get_startup(self):
        # If file not exists
        if(not os.path.exists(self.SERVICE_FILE)):
            # Return None
            return None
        # Open file
        with open(self.SERVICE_FILE, "r") as f:
            # Return full key
            return f.readlines()[8][37:-1]
