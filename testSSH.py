import os
import subprocess
import sys

import paramiko


def ssh_send(hn, p, u, pw):
    if os.path.isfile(pw):
        with open(pw, 'r') as passFile:
            pw = passFile.readline()
    ssh = paramiko.SSHClient()

    print(pw)
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(hostname=hn, port=p, username=u,
                password=pw, timeout=3)

    this_dir = str(subprocess.check_output(['pwd']))[2:-3] + "/"
    this_file = this_dir + os.path.basename(__file__)
    print(this_file)

    ftp_client = ssh.open_sftp()
    ftp_client.put(this_file, '/home/matija/testSSH.py')
    ftp_client.close()
    stdin, stdout, stderr = ssh.exec_command("python3 /home/matija/testSSH.py")
    print(stdout.readlines())
    del ftp_client, stdin, stdout, stderr


if sys.argv[0] == '/home/matija/testSSH.py':  # server prima fajl
    print("svasta")
else:
    ssh_send('192.168.122.17', 22, 'root', "IP/pw")
