import platform
from wallme.managers.linux import Linux
from wallme.managers.windows import Windows
from wallme.exceptions import WallmeException

class ManagerFactory():

	def get_manager(self):
		system = platform.system()
		if(system == "Linux"):
			return Linux()
		elif(system == "Windows"):
			return Windows()
		else:
			raise WallmeException("Unknown system : '" + system + "'")