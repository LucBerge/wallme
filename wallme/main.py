import traceback, argparse
from wallme.websites import WEBSITES
from wallme.websites.websitefactory import WebsiteFactory
from wallme.managers.managerfactory import ManagerFactory
from wallme.exceptions import WallmeException

def main():

	parser = argparse.ArgumentParser(description='Change your desktop wallpaper based on websites.')
	parser.add_argument('-list', action='store_true', help='list all the available websites')
	parser.add_argument('-info', type=str, help='open the webpage on which the image is taken from')
	parser.add_argument('-set', type=str, help='change the wallpaper')
	parser.add_argument('-set-startup', type=str, help='change your wallpaper on startup')
	parser.add_argument('-unset-startup', action='store_true', help='stop changing your wallpaper on startup')
	args = parser.parse_args()
    
	try:
		if(args.list):
			for name in WEBSITES.keys():
				print(name + " - " + WEBSITES[name].DESCRIPTION)
		else:
			manager_factory = ManagerFactory()
			manager = manager_factory.get_manager()
        
			if(args.unset_startup):
				manager.unset_startup()
			else:
				website_factory = WebsiteFactory()
				if(args.set):
					website = website_factory.get_website(args.set)
					manager.set(website)
				if(args.set_startup):
					website = website_factory.get_website(args.set_startup)
					manager.set_startup(website)
				if(args.info):
					website = website_factory.get_website(args.info)
					manager.info(website)
    
	except WallmeException as e:
		print(e)
	except Exception as e:
		traceback.print_exc()
		print("=========\nPlease, report this issue : https://github.com/LucBerge/wallme/issues")

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		None