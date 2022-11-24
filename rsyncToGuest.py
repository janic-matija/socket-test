import sys
import time
import os
import subprocess


def active_ips():
    addresses = []
    command = 'virsh list --name'
    vms = str(subprocess.check_output(command.split()).decode("utf-8")).splitlines()
    for i in range(0, len(vms) - 1):
        command = 'virsh domifaddr ' + str(vms[i])
        info = (str(subprocess.check_output(command.split()).decode("utf-8"))).splitlines()
        for j in range(2, len(info) - 1):
            addresses.append(info[j].split()[3].split('/')[0])
    return addresses


def main():
    start = time.time()
    start_time = start
    if len(sys.argv) > 1 and os.path.isdir(sys.argv[1]):
        send_to = active_ips()
        if len(sys.argv) > 2:
            send_to = ['10.18.110.57']
        print(send_to)
        for ip in send_to:
            print(ip)
            com = "rsync -a " + sys.argv[1] + " root@" + ip + ":/tempdir2"
            # os.system(com)
            subprocess.run(com.split())
            print(time.time() - start_time, end="\n\n")
            start_time = time.time()
        print(time.time() - start)
        return
    print('rsync needs a path as argument')


if __name__ == "__main__":
    main()

# example: python3 rsyncToGuest.py /home/matija/Projects/socket-test/socket-test/data
