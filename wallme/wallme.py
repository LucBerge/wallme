import sys
from websites import WEBSITES
from manager import *

########
# MAIN #
########

def main(name):
	try :
		manager = Manager(name)
		manager.wallme()
		print("New wallpaper set.")
	except Exception as e:
		print(e)

##########
# GLOBAL #
##########

def list():
	for name in WEBSITES.keys():
		print(name + " - " + WEBSITES[name].DESCRIPTION)

def help():
	print("Usage:\n'" + sys.argv[0] + " <WEBSITE>'\n\nOptions:\n -l --list To list supported websites.")

if __name__ == "__main__":
	try:
		if(len(sys.argv) == 2):
			if(sys.argv[1] == "-l" or sys.argv[1] == "--list"):
				list()
			else:
				main(sys.argv[1])
		else:
			help()
	except KeyboardInterrupt:
		None