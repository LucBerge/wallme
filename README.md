[![release](https://img.shields.io/badge/release-1.0-succes.svg)](https://pypi.org/project/wallme/)

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
import re

NAME = 'apod'
DESCRIPTION = 'Astronomy Picture of the Day'

def getWebPageUrl():
	return 'https://apod.nasa.gov/apod/astropix.html'

def getPictureUrl(webpage):
	pictureurl = re.search("""<IMG SRC="(.*?)"[^>]*?>""",webpage)

	if(pictureurl == None):
		raise Exception("No image found today. It could be a video.")

	return 'https://apod.nasa.gov/apod/' + pictureurl.group(1)
```

4. Import your file in websites.py

5. Develop the package
```
python3 setup.py develop --user
```

6. Check if it works by calling 
```
wallme <WEBSITE>
```

7. Pull request

## Contact

Please contact [@LucBerge](https://github.com/LucBerge) for more informations.
