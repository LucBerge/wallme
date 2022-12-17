# coding: utf8

import ctypes
import winreg
from .manager import Manager
from ..exceptions import WallmeException
from .. import utils
import os


class Windows(Manager):

    REGISTRY_KEY = "wallme"
    DATA_FOLDER = os.path.expandvars(r'%LOCALAPPDATA%\Wallme')

    def __init__(self, entry_point):
        super().__init__(entry_point, self.DATA_FOLDER)

    def set(self, full_key, test=False):
        image_path = super().download(full_key, False, test=test)
        if (not test):
            if ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3) != 1:
                error = ctypes.GetLastError()
                raise WallmeException("Cannot set wallpaper: " + str(error))

    def set_startup(self, full_key):
        # Check the full key is correct
        utils.get_website_subkey_from_fullkey(full_key)
        # Set startup
        reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Run', 0, winreg.KEY_SET_VALUE)
        with reg_key:
            winreg.SetValueEx(reg_key, self.REGISTRY_KEY, 0, winreg.REG_SZ, "cmd /c start /min " + self.entry_point + " -set " + full_key)

    def unset_startup(self):
        reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Run', 0, winreg.KEY_SET_VALUE)
        with reg_key:
            winreg.DeleteValue(reg_key, self.REGISTRY_KEY)

    def get_startup(self):
        try:
            reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Run', 0, winreg.KEY_READ)
            with reg_key:
                # Get line
                values = winreg.QueryValueEx(reg_key, self.REGISTRY_KEY)[0].split(' ')
                # Return entry point and full key
                return " ".join(values[4:-2]), values[-1]
        except FileNotFoundError:
            return None, None
