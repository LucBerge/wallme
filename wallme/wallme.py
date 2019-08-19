import sys
from wallme.websites import WEBSITES
from wallme.manager import *

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

def parse():
	if(len(sys.argv) == 2):
		if(sys.argv[1] == "-l" or sys.argv[1] == "--list"):
			list()
		else:
			main(sys.argv[1])
	else:
		help()

def list():
	for name in WEBSITES.keys():
		print(name + " - " + WEBSITES[name].DESCRIPTION)

def help():
	print("Usage:\n\twallme <WEBSITE>\n\nOptions:\n -l --list To list supported websites.")

if __name__ == "__main__":
	try:
		parse()
	except KeyboardInterrupt:
		None