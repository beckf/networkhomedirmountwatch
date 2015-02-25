# Luggage Makefile
# http://wiki.github.com/unixorn/luggage/

include /usr/local/share/luggage/luggage.make

TITLE=networkhomedirmountwatch
REVERSE_DOMAIN=org.da

PAYLOAD=\
        pack-scriptPy\
	pack-Library-LaunchDaemons-org.da.networkhomedirmountwatch.plist\
	pack-script-preinstall\
	pack-script-postinstall

PACKAGE_VERSION=0.3

pack-scriptPy: l_usr_local_bin
	@sudo ${CP} ./networkhomedirmountwatch.py ${WORK_D}/usr/local/bin/networkhomedirmountwatch.py
	@sudo chmod 755 ${WORK_D}/usr/local/bin/networkhomedirmountwatch.py
	@sudo chown root:wheel ${WORK_D}/usr/local/bin/networkhomedirmountwatch.py
