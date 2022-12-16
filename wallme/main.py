# coding: utf8

import traceback
import argparse
import sys
from .websites import WEBSITES
from .managers.managerfactory import ManagerFactory
from .exceptions import WallmeException
from .log import logger
from .gui import Gui


def main():

    parser = argparse.ArgumentParser(description='Change your desktop wallpaper based on websites.')
    parser.add_argument('-list', action='store_true', help='list all the available websites')
    parser.add_argument('-info', type=str, help='open the webpage on which the image is taken from')
    parser.add_argument('-url', type=str, help='gets the url of the image')
    parser.add_argument('-set', type=str, help='change the wallpaper')
    parser.add_argument('-set-startup', type=str, help='change your wallpaper on startup')
    parser.add_argument('-unset-startup', action='store_true', help='stop changing your wallpaper on startup')
    parser.add_argument('-prank', action='store_true', help='prank your friends')
    args = parser.parse_args()

    if (len(sys.argv) <= 1):
        gui = Gui()
        gui.resizable(False, False)
        gui.mainloop()
    else:
        if (args.list):
            for key in WEBSITES.keys():
                logger.debug(key + " - " + WEBSITES[key].description)
        else:
            manager_factory = ManagerFactory()
            manager = manager_factory.get_manager()

            if (args.unset_startup):
                manager.unset_startup()
            else:
                if (args.info):
                    manager.info(args.info)
                if (args.url):
                    manager.url(args.url)
                if (args.set):
                    manager.set(args.set)
                if (args.set_startup or args.prank):
                    if (args.prank):
                        manager.prank()
                    else:
                        manager.set_startup(args.set_startup)


if __name__ == "__main__":
    try:
        main()
    except PermissionError:
        logger.error("You need admin permission to run this command")
    except WallmeException as e:
        logger.error(str(e))
    except Exception:
        traceback.print_exc()
        logger.error("Please, report this issue : https://github.com/LucBerge/wallme/issues")
    except KeyboardInterrupt:
        None
