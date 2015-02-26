# networkhomedirmountwatch
This Launch Daemon was created to help fix a problem introduced in Mac OS 10.9 that prevents
Network Homes from getting unmounted at logout.  Processes like mdworker (SpotLight) continue to use the 
mounted home thus preventing it from being unmounted.  Sometimes the home is unmounted at logout, but remounted
by a stale proccess.  This Launch Daemon will run every 5 minutes on the computer to check for mounted homes
that are not currently in use by a logged in user.  All processes for the logged out user are killed and the home
is forcibly unmounted.

# Installing
Use Luggage to build a package.
make pkg
