# coding: utf8

import sys
import setuptools

if sys.version_info < (3, 5):
    sys.exit('wallme requires Python 3.5+')

with open('requirements.txt', 'r') as f:
    requirements = [
        s for s in [
            line.split('#', 1)[0].strip(' \t\n') for line in f
        ] if s != ''
    ]

long_description = open("README.md", "r").read()

setuptools.setup(
    name='wallme',
    version='1.7',
    author='LucBerge',
    author_email='lucas.bergeron@outlook.fr',
    description="Change your wallpaper every day",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/LucBerge/wallme',
    packages=setuptools.find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': ['wallme=wallme.main:main'],
    }
)
