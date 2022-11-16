import sys
import time
import os
import subprocess


def output(com):
    info = str(subprocess.check_output(com.split()).decode("utf-8"))
    info_rows = info.splitlines()
    addresses = []
    ip_info = []
    ips = []
    if len(info_rows) > 3:  # active
        for i in range(2, len(info_rows) - 1):
            addresses.append(info_rows[i].split())
        for addr in addresses:
            ip_info.append(addr)
        for ip in ip_info:
            ips.append(ip[3].split('/')[0])
    return ips


def main():
    if len(sys.argv) > 1 and os.path.isdir(sys.argv[1]):

        start = time.time()
        command = 'virsh list --name'
        vms = str(subprocess.check_output(command.split()).decode("utf-8")).splitlines()
        send_to = []
        if len(vms) > 1:
            for i in range(0, len(vms) - 1):
                command = 'virsh domifaddr ' + str(vms[i])
                send_to.append(output(command))
        print(send_to)
        # os.system("rsync -a " + sys.argv[1] + " root@" + ip + ":/tempdir")

        print(time.time() - start)


if __name__ == "__main__":
    main()

# python3 test.py /home/matija/Projects/socket-test/socket-test/data
