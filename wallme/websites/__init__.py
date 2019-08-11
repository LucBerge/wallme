import wallme.websites.websites, types

WEBSITES = {}

for item in list(globals().items()):
	if(isinstance(item, tuple)):
		if(isinstance(item[1], types.ModuleType)):
			if("websites." in item[1].__name__ and item[1].__name__ != "wallme.websites.websites"):
				WEBSITES[item[1].NAME] = item[1]