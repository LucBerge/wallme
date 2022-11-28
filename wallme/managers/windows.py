# coding: utf8

import ctypes
import winreg
from .manager import Manager
from ..exceptions import WallmeException
import os


class Windows(Manager):

    REGISTRY_KEY = "wallme"
    DATA_FOLDER = os.path.expandvars(r'%LOCALAPPDATA%\Wallme')

    def __init__(self):
        super().__init__(self.DATA_FOLDER)

    def set(self, full_key, test=False):
        super().download(full_key, test)
        if(not test):
            if ctypes.windll.user32.SystemParametersInfoW(20, 0, self.image, 3) != 1:
                raise WallmeException("Cannot set wallpaper")

    def set_startup(self, full_key):
        reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Run', 0, winreg.KEY_SET_VALUE)
        with reg_key:
            winreg.SetValueEx(reg_key, self.REGISTRY_KEY, 0, winreg.REG_SZ, "cmd /c start /min wallme.exe -set " + full_key)

    def unset_startup(self):
        reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Run', 0, winreg.KEY_SET_VALUE)
        with reg_key:
            winreg.DeleteValue(reg_key, self.REGISTRY_KEY)

    def get_startup(self):
        try:
            reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Run', 0, winreg.KEY_READ)
            with reg_key:
                value = winreg.QueryValueEx(reg_key, self.REGISTRY_KEY)[0]
                return value.split(' ')[-1]
        except FileNotFoundError:
            return None
