# coding: utf8

from .apod import Apod
from .astrobin import Astrobin
from .bing import Bing
from .epod import Epod
from .nasa import Nasa
from .national_geographic import NationalGeographic
from .reddit import Reddit
from .tetras import Tetras
from .the_guardian import TheGuardian
from .the_telegraph import TheTelegraph
from .wikipedia import Wikipedia
from .windows_spotlight import WindowsSpotlight

WEBSITES = {}
WEBSITES[Apod.key] = Apod()
WEBSITES[Astrobin.key] = Astrobin()
WEBSITES[Bing.key] = Bing()
WEBSITES[Epod.key] = Epod()
WEBSITES[Nasa.key] = Nasa()
WEBSITES[NationalGeographic.key] = NationalGeographic()
WEBSITES[Reddit.key] = Reddit()
WEBSITES[Tetras.key] = Tetras()
WEBSITES[TheGuardian.key] = TheGuardian()
WEBSITES[TheTelegraph.key] = TheTelegraph()
WEBSITES[Wikipedia.key] = Wikipedia()
WEBSITES[WindowsSpotlight.key] = WindowsSpotlight()
