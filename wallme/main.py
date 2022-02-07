# coding: utf8

import traceback
import argparse
import sys
from . import utils
from .websites import WEBSITES
from .websites.websitefactory import WebsiteFactory
from .managers.managerfactory import ManagerFactory
from .exceptions import WallmeException

PRANK_KEY = "reddit.sexywomanoftheday"


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

    if(len(sys.argv) <= 1):
        parser.print_help()
    else:
        try:
            if(args.list):
                for key in WEBSITES.keys():
                    print(key + " - " + WEBSITES[key].DESCRIPTION)
            else:
                manager_factory = ManagerFactory()
                manager = manager_factory.get_manager()

                if(args.unset_startup):
                    manager.unset_startup()
                else:
                    website_factory = WebsiteFactory()
                    if(args.info):
                        key, subkey = utils.get_key_subkey_from_fullkey(args.info)
                        website = website_factory.get_website(key)
                        manager.info(website, subkey)
                    if(args.url):
                        key, subkey = utils.get_key_subkey_from_fullkey(args.url)
                        website = website_factory.get_website(key)
                        manager.url(website, subkey)
                    if(args.set):
                        key, subkey = utils.get_key_subkey_from_fullkey(args.set)
                        website = website_factory.get_website(key)
                        manager.set(website, subkey)
                    if(args.set_startup or args.prank):
                        if(args.prank):
                            args.set_startup = PRANK_KEY
                        key, subkey = utils.get_key_subkey_from_fullkey(args.set_startup)
                        website = website_factory.get_website(key)
                        manager.set_startup(website, subkey)

        except PermissionError:
            print("You need admin permission to run this command")
        except WallmeException as e:
            print(e)
        except Exception:
            traceback.print_exc()
            print("=========\nPlease, report this issue : https://github.com/LucBerge/wallme/issues")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        None
