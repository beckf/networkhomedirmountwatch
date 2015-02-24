VER=0.1
IDENTIFIER=org.da.networkhomedirmountwatch
SCRIPTNAME=networkhomedirmountwatch.py

networkhomedirmountwatch.pkg: $(SCRIPTNAME) $(IDENTIFIER).plist postinstall preinstall
	rm -rf pkgroot pkgscripts
	mkdir pkgroot pkgscripts

	cp postinstall preinstall pkgscripts/
	mkdir -p pkgroot/{Library/LaunchDaemons,usr/local/bin}
	cp $(SCRIPTNAME) pkgroot/usr/local/bin
	cp $(IDENTIFIER).plist pkgroot/Library/LaunchDaemons
	xattr -cr pkgroot pkgscripts

	pkgbuild --version $(VER) --scripts pkgscripts --root pkgroot --identifier $(IDENTIFIER) $@

clean:
	rm -rf *.pkg *.dmg pkgroot pkgscripts
