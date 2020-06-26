import ctypes, os
try:
    import winreg
except:
    pass
from .manager import Manager
from ..exceptions import WallmeException

class Windows(Manager):

    REGISTRY_KEY = "wallme"

    def set(self, website, test=False):
        super().download(website)
        if(not test):
            if ctypes.windll.user32.SystemParametersInfoW(20, 0, self.IMAGE, 3) != 1:
                raise WallmeException("Cannot set wallpaper")

    def set_startup(self, website):
        reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Run', 0, winreg.KEY_SET_VALUE)
        with reg_key:
            winreg.SetValueEx(reg_key, self.REGISTRY_KEY, 0, winreg.REG_SZ, "cmd /c start /min wallme.exe -set " + website.KEY + '.' + website.subkey)
            
    def unset_startup(self):
        reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Run', 0, winreg.KEY_SET_VALUE)
        with reg_key:
            winreg.DeleteValue(reg_key, self.REGISTRY_KEY)