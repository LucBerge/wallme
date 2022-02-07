[![release](https://img.shields.io/pypi/v/wallme)](https://pypi.org/project/wallme/)
[![test](https://img.shields.io/github/workflow/status/LucBerge/wallme/Test?branch=dev&label=Test)](https://github.com/LucBerge/wallme/actions/workflows/test.yml)
[![Deploy](https://img.shields.io/github/workflow/status/LucBerge/wallme/CD?branch=master&label=Deploy)](https://github.com/LucBerge/wallme/actions/workflows/cd.yml)
[![coverage](https://codecov.io/gh/LucBerge/wallme/branch/dev/graph/badge.svg?token=AH8jbVSPj3)](https://codecov.io/gh/LucBerge/wallme)

# wallme

## Description

wallme is a python tool that change your wallpaper every day based on websites.

## Prerequisites

Pip installation :
```
python3 get-pip.py
```

## Install

From [PyPi](https://pypi.org/project/wallme/) :
```
pip install wallme
```

## Update
```
pip install wallme -U
```

## Uninstall

```
pip uninstall wallme
```

## Usage

List all the available websites :
```
wallme -list
```
Open the webpage on which the image is taken from :
```
wallme -info <website>
```
Retrieve the image url from the website :
```
wallme -url <website>
```
Change the wallpaper :
```
wallme -set <website>
```
Change your wallpaper on startup :
```
wallme -set-startup <website>
```
Stop changing your wallpaper on startup :
```
wallme -unset-startup
```

## Contribute by adding a new website

1. Fork

2. Create a new branch and checkout

3. Create a new file from template

```python
from wallme import utils

NAME = 'apod'
DESCRIPTION = 'Astronomy Picture of the Day'
URL = 'https://apod.nasa.gov/apod/astropix.html'

def pre_process():
	return None
    
def process(date):
	soup = utils.get_soup_from_url(URL)
	imgs = utils.find_tags_from_soup(soup, "img")
	return 'https://apod.nasa.gov/apod/' + imgs[0].get('src')
    
def post_process(image):
	return None
```

4. Import your file in websites.py

5. Check if it works by calling 
```
python main.py <WEBSITE>
```

7. Commit and pull request

## Contact

Please contact [@LucBerge](https://github.com/LucBerge) for more informations.
