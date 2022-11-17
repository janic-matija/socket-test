#startup.service

	$ sudo mv dirFromHost.py /etc/systemd/system
	$ sudo systemctl enable startup.service
	$ sudo systemctl start startup.service
##1 socket

	#dirFromHost.py
		Guest: autostart (startup.service)
	#dirToGuest.py
		Host: executable?

##2 socket
	#sendDir.py
		ssh slanje skripte (bez autostart)
##3 rsync
	#rsyncToGuest.py
		rsync slanje aktivnim Guest-ovima (bez autostart)
