import platform
from ..exceptions import WallmeException
from .linux import Linux
from .windows import Windows

class ManagerFactory():

    def get_manager(self):
        system = platform.system()
        if(system == "Linux"):
            return Linux()
        elif(system == "Windows"):
            return Windows()
        else:
            raise WallmeException("Unknown system : '" + system + "'")