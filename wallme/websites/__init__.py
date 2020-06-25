import types

import wallme.websites.apod
import wallme.websites.astrobin
import wallme.websites.bing
import wallme.websites.epod
import wallme.websites.nasa
import wallme.websites.nationalgeographic
import wallme.websites.tetras
import wallme.websites.theguardian
import wallme.websites.thetelegraph
import wallme.websites.wikipedia

WEBSITES = {}

for item in list(globals().items()):
	if(isinstance(item, tuple)):
		if(isinstance(item[1], types.ModuleType)):
			if("websites." in item[1].__name__):
				WEBSITES[item[1].NAME] = item[1]