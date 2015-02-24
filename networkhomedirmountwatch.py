#!/usr/bin/python

import subprocess
import sys
import os
import syslog


def check_call_with_errhandler(cmd):
    try:
        subprocess.check_call(cmd)
    except subprocess.CalledProcessError as err:
        syslog.syslog(syslog.LOG_ALERT, '%s: %s' % (err, err.message))


def log(msg):
    syslog.syslog(syslog.LOG_ALERT, msg)


syslog.openlog('NetworkHomeDirMountWatch')

# Is there a .localized folder hidden here?
mountedHomes = os.listdir('/home')
consoleUsers = subprocess.check_output(['/usr/bin/users']).split()
networkConsoleUsers = [user for user in consoleUsers if user in mountedHomes]

for home in mountedHomes:
    if home in networkConsoleUsers:
        log('User %s still logged in.' % home)
    else:
        log('Killing processes for %s.' % home)
        check_call_with_errhandler(['/usr/bin/killall' ,'-9', '-u', home])

        log('Forcing unmount of network home ' 'for %s.' % home)
        homeDir = os.path.join('/home', home)
        check_call_with_errhandler(['/sbin/umount', '-f', homeDir])
