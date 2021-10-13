
all:
	
install:
	install -d $(D)/usr/lib/enigma2/python/Plugins/SystemPlugins/LCNScanner/
	install -m 644 src/*.py $(D)/usr/lib/enigma2/python/Plugins/SystemPlugins/LCNScanner/
	install -m 644 rules.xml $(D)/usr/lib/enigma2/python/Plugins/SystemPlugins/LCNScanner/
	