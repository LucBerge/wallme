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
WEBSITES[astrobin.KEY] = astrobin
WEBSITES[bing.KEY] = bing
WEBSITES[epod.KEY] = epod
WEBSITES[nasa.KEY] = nasa
WEBSITES[nationalgeographic.KEY] = nationalgeographic
WEBSITES[reddit.KEY] = reddit
WEBSITES[tetras.KEY] = tetras
WEBSITES[theguardian.KEY] = theguardian
WEBSITES[thetelegraph.KEY] = thetelegraph
WEBSITES[wikipedia.KEY] = wikipedia
