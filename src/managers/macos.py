# coding: utf8

import subprocess
from .manager import Manager
from ..exceptions import WallmeException


class MacOS(Manager):

    SET_SCRIPT = """/usr/bin/osascript<<END
                            tell application "Finder"
                            set desktop picture to POSIX file "%s"
                            end tell
                            END"""

    def set(self, website, subkey, test=False):
        super().download(website, subkey)
        if(not test):
            print("=====" + subprocess.Popen(self.SET_SCRIPT % self.IMAGE, shell=True) + "=======")
            # if subprocess.Popen(self.SET_SCRIPT%self.IMAGE, shell=True) != 0:
            #     raise WallmeException("Cannot set wallpaper")
            # https://stackoverflow.com/questions/431205/how-can-i-programmatically-change-the-background-in-mac-os-x
            # https://stackoverflow.com/questions/29338066/run-python-script-at-os-x-startup

    def set_startup(self, website, subkey):
        self.unset_startup()
        if subkey:
            fullkey = website.KEY + '.' + subkey
        else:
            fullkey = website.KEY
        # TO DO

    def unset_startup(self):
        # TO DO
        pass
