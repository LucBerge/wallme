# coding: utf8

import sys
import setuptools

if sys.version_info < (3, 5):
    sys.exit('wallme requires Python 3.5+')

long_description = open("README.md", "r").read()

setuptools.setup(
    name='wallme',
    version='1.5.1',
    author='LucBerge',
    author_email='lucas.bergeron@outlook.fr',
    description="Change your wallpaper every day",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/LucBerge/wallme',
    packages=setuptools.find_packages(),
    install_requires=['requests', 'bs4', 'Pillow', 'pathlib'],
    entry_points={
        'console_scripts': ['wallme=wallme.main:main'],
    }
)
