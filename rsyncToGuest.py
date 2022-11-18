import sys
import time
import os
import subprocess


def active_ips():
    addresses=[]
    command = 'virsh list --name'
    vms = str(subprocess.check_output(command.split()).decode("utf-8")).splitlines()
    for i in range(0, len(vms) - 1):
        command = 'virsh domifaddr ' + str(vms[i])
        info = (str(subprocess.check_output(command.split()).decode("utf-8"))).splitlines()
        for i in range(2, len(info) - 1):
            addresses.append(info[i].split()[3].split('/')[0])
    return addresses
    

def main():
    if len(sys.argv) > 1 and os.path.isdir(sys.argv[1]):
        start = time.time()
        send_to=active_ips()
        print(send_to)
        #for ip in send_to:
        #    os.system("rsync -a " + sys.argv[1] + " root@" + ip + ":/tempdir")
        print(time.time() - start)
        return
    print('rsync needs path to folder as argument')


if __name__ == "__main__":
    main()

# example: python3 rsyncToGuest.py /home/matija/Projects/socket-test/socket-test/data
