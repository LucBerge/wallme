
[![Version](https://img.shields.io/pypi/v/wallme?label=Version)](https://github.com/LucBerge/wallme/releases)
[![Downloads](https://img.shields.io/github/downloads/lucberge/wallme/total?label=Downloads)](https://github.com/LucBerge/wallme/releases)
[![test](https://img.shields.io/github/workflow/status/LucBerge/wallme/Test?branch=dev&label=Test)](https://github.com/LucBerge/wallme/actions/workflows/test.yml)
[![Deploy](https://img.shields.io/github/workflow/status/LucBerge/wallme/CD?branch=master&label=Deploy)](https://github.com/LucBerge/wallme/actions/workflows/cd.yml)
[![coverage](https://codecov.io/gh/LucBerge/wallme/branch/dev/graph/badge.svg?token=AH8jbVSPj3)](https://codecov.io/gh/LucBerge/wallme)

<p align="center">
  <img width="1000" src="images/example.gif">
</p>

[![Pypi](https://img.shields.io/badge/Install_from-pypi-blue)](https://pypi.org/project/wallme/)
[![GitHub](https://img.shields.io/badge/Install_from-GitHub-lightgrey?logo=github)](https://github.com/LucBerge/wallme/releases)

# wallme

## Description

Wallme is a python tool to change your wallpaper every day based on websites. You can check WEBSITES.md for a full list ad supported websites (comming soon).

## From CLI
### Install / Update

From [PyPi](https://pypi.org/project/wallme/) :
```
pip install wallme -U
```

### Uninstall
```
pip uninstall wallme
```

### Usage

Open the GUI:
```
wallme
```
Display the help:
```
wallme -h
```
List all the available websites:
```
wallme -list
```
Open the webpage on which the image is taken from:
```
wallme -info <website>
```
Retrieve the image url from the website:
```
wallme -url <website>
```
Change the wallpaper:
```
wallme -set <website>
```
Change your wallpaper on startup:
```
wallme -set-startup <website>
```
Stop changing your wallpaper on startup:
```
wallme -unset-startup
```
Prank your friends:
```
wallme -prank
```

## From CLI
### Install
[Download the latest release on github](https://github.com/LucBerge/wallme/releases).

### Usage
Double click the exe file to open the GUI.

## Contribute by adding a new website

1. Fork

2. Create a new branch and checkout

3. Create a new file from [template](https://github.com/LucBerge/wallme/blob/master/wallme/websites/nasa.py)
```python
# coding: utf8

from .website import Website


class Nasa(Website):
    key = 'nasa'
    description = 'Pictures related to Nasa\'s missions'
    url = 'https://www.nasa.gov/multimedia/imagegallery/iotd.html'

    def process(self, date, subkey):
        json = self.get_json_from_url('https://www.nasa.gov/api/2/ubernode/_search?size=1&from=0&sort=promo-date-time%3Adesc&q=((ubernode-type%3Aimage)%20AND%20(routes%3A1446))&_source_include=promo-date-time%2Cmaster-image%2Cnid%2Ctitle%2Ctopics%2Cmissions%2Ccollections%2Cother-tags%2Cubernode-type%2Cprimary-tag%2Csecondary-tag%2Ccardfeed-title%2Ctype%2Ccollection-asset-link%2Clink-or-attachment%2Cpr-leader-sentence%2Cimage-feature-caption%2Cattachments%2Curi')
        uri = json['hits']['hits'][0]['_source']['master-image']['uri']
        return "https://www.nasa.gov/sites/default/files/styles/full_width_feature/public/" + uri.replace("public://", "")
```

4. Import your file in `__init__.py`

5. Create a new test from [template](https://github.com/LucBerge/wallme/blob/master/test/test_nasa.py)
```python
# coding: utf8

from .test_website import TestWebsite


class TestNasa(TestWebsite):
    def test_info(self):
        self._test_info("nasa")

    def test_url(self):
        self._test_url("nasa")

    def test_set(self):
        self._test_set("nasa")

    def test_set_unset_startup(self):
        self._test_set_unset_startup("nasa")
```

6. Test your code by calling 
```
pytest test/test_nasa.py
```

7. Commit and pull request

## Contact

Please contact [@LucBerge](https://github.com/LucBerge) for more informations.
