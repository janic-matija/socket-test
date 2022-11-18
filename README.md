# listening.service

	$ sudo mv listening.service /etc/systemd/system
    $ sudo mv dirFromHost.py /bin
	$ sudo systemctl enable listening.service
	$ sudo systemctl start listening.service

# #1 socket
# 	dirFromHost.py
	Guest: autostart (startup.service)
# 	dirToGuest.py
	Host: executable?

# #2 socket
#	sendDir.py
	ssh slanje skripte (bez autostart)

# #3 rsync
# 	rsyncToGuest.py
	rsync slanje aktivnim Guest-ovima (bez autostart)
