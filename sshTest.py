#!/usr/bin/env python3
import subprocess
import sys
import time
import socket
import os

import paramiko

GUEST = "192.168.122.17"
PORT = 22
USER = 'root'


def ssh_send(hn, p, u):
    ssh = paramiko.SSHClient()

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(hostname=hn, port=p, username=u, timeout=3)

    this_dir = str(subprocess.check_output(['pwd']))[2:-3] + "/"  # trenutni folder
    this_file = this_dir + os.path.basename(__file__)  # ime skripte
    print(this_file)

    ftp_client = ssh.open_sftp()

    ftp_client.put(this_file, '/tempdir/test.py')
    ftp_client.close()


def main():
    ssh_send(GUEST, PORT, USER)


if __name__ == "__main__":
    main()
