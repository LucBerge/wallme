# coding: utf8

from . import apod
from . import astrobin
from . import bing
from . import epod
from . import nasa
from . import national_geographic
from . import outdoor_photographer
from . import reddit
from . import tetras
from . import the_guardian
from . import the_telegraph
from . import wikipedia
from . import windows_spotlight

WEBSITES = {}
WEBSITES[apod.KEY] = apod
WEBSITES[astrobin.KEY] = astrobin
WEBSITES[bing.KEY] = bing
WEBSITES[epod.KEY] = epod
WEBSITES[nasa.KEY] = nasa
WEBSITES[national_geographic.KEY] = national_geographic
WEBSITES[outdoor_photographer.KEY] = outdoor_photographer
WEBSITES[reddit.KEY] = reddit
WEBSITES[tetras.KEY] = tetras
WEBSITES[the_guardian.KEY] = the_guardian
WEBSITES[the_telegraph.KEY] = the_telegraph
WEBSITES[wikipedia.KEY] = wikipedia
WEBSITES[windows_spotlight.KEY] = windows_spotlight
