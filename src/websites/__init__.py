# coding: utf8

from . import apod
from . import astrobin
from . import bing
from . import epod
from . import nasa
from . import nationalgeographic
from . import reddit
from . import tetras
from . import theguardian
from . import thetelegraph
from . import wikipedia

WEBSITES = {}
WEBSITES[apod.KEY] = apod
WEBSITES[apod.KEY] = astrobin
WEBSITES[apod.KEY] = bing
WEBSITES[apod.KEY] = epod
WEBSITES[apod.KEY] = nasa
WEBSITES[apod.KEY] = nationalgeographic
WEBSITES[apod.KEY] = reddit
WEBSITES[apod.KEY] = tetras
WEBSITES[apod.KEY] = theguardian
WEBSITES[apod.KEY] = thetelegraph
WEBSITES[apod.KEY] = wikipedia
