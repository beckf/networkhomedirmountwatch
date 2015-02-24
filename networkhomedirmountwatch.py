#!/usr/bin/python

import subprocess
import sys
import os
import syslog

syslog.openlog('NetworkHomeDirMountWatch')

mountedHomes = os.listdir('/home')
consoleUsers = subprocess.check_output(['/usr/bin/users'])

for home in mountedHomes:
	try:
		if home in consoleUsers:
			syslog.syslog(syslog.LOG_ALERT, 'User ' + home + ' still logged in.')
		else:
			syslog.syslog(syslog.LOG_ALERT, 'Killing processes for ' + home + '.')
			homeDir = '/home/' + home
			subprocess.call(['/usr/bin/killall' ,'-9', '-u', home])
			syslog.syslog(syslog.LOG_ALERT, 'Forcing unmount of network home for ' + home + '.')
			subprocess.call(['/sbin/umount', '-f', homeDir]) 
	except:
		print error


