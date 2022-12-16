# coding: utf8

import os
from .manager import Manager
from ..exceptions import WallmeException
from .. import utils


class Linux(Manager):

    USER = os.environ.get('SUDO_USER', os.environ.get('USERNAME'))
    DATA_FOLDER = os.path.expanduser(f'~' + USER) + "/wallme"
    SERVICE_FILE = "/lib/systemd/system/wallme.service"

    def __init__(self, entry_point):
        if(not utils.is_admin()):
            raise PermissionError()
        if('.py' in entry_point):
            entry_point = os.popen('sudo runuser -l ' + self.USER + ' -c "which wallme"').read().rstrip()
        super().__init__(entry_point, self.DATA_FOLDER)

    def set(self, full_key, test=False):
        image_path = super().download(full_key, False, test=test)
        if (not test):
            if os.system("sudo /usr/bin/gsettings set org.gnome.desktop.background picture-uri " + image_path) != 0:
                raise WallmeException("Cannot set wallpaper")

    def set_startup(self, full_key):
        self.unset_startup()
        if (not os.path.exists(self.SERVICE_FILE)):
            with open(self.SERVICE_FILE, "wt") as f:
                f.write("[Unit]\n\
Description=Wallme service.\n\
After=network-online.target\n\
\n\
[Service]\n\
Type=simple\n\
User=" + self.USER + "\n\
Group=" + self.USER + "\n\
ExecStart=" + self.entry_point + " -set " + full_key + "\n\
\n\
[Install]\n\
WantedBy=multi-user.target")
        os.system("sudo systemctl enable wallme")

    def unset_startup(self):
        if (os.path.exists(self.SERVICE_FILE)):
            os.remove(self.SERVICE_FILE)
            os.system("sudo systemctl disable wallme")

    def get_startup(self):
        # If file not exists
        if (not os.path.exists(self.SERVICE_FILE)):
            # Return None
            return None
        # Open file
        with open(self.SERVICE_FILE, "r") as f:
            # Return full key
            return f.readlines()[8].split(' ')[-1][:-1]
