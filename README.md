[![release](https://img.shields.io/badge/release-1.2-succes.svg)](https://pypi.org/project/wallme/)

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

```
wallme <WEBSITE>
```

## Contribute by adding a new website

1. Fork

2. Create a new branch and checkout

3. Create a new file from template

```python
from wallme import utils

NAME = 'apod'
DESCRIPTION = 'Astronomy Picture of the Day'

def pre_process():
	return None
    
def process(date):
	soup = utils.get_soup_from_url('https://apod.nasa.gov/apod/astropix.html')
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
