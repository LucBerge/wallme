import types

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

for item in list(globals().items()):
	if(isinstance(item, tuple)):
		if(isinstance(item[1], types.ModuleType)):
			if("websites." in item[1].__name__):
				WEBSITES[item[1].KEY] = item[1]