# coding: utf8

import platform
from ..exceptions import WallmeException

system = platform.system()
if(system == "Linux"):
    from .linux import Linux as M
elif system == "Windows":
    from .windows import Windows as M
elif system == "Darwin":
    from .macos import MacOS as M


class ManagerFactory():

    def get_manager(self):
        try:
            return M()
        except NameError:
            raise WallmeException("Unknown system : '" + platform.system() + "'. This is not a bug, you just found a new platform on which wallme might not be working. Help us improving the software by reporting this message : https://github.com/LucBerge/wallme/issues")
