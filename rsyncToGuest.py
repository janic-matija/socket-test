import sys
import time
import os
import subprocess


def output(com):
    info = str(subprocess.check_output(com.split()).decode("utf-8"))
    info_rows = info.splitlines()
    info_list = []
    if len(info_rows) > 3:  # active
        for i in range(2, len(info_rows) - 1):
            info_list.append(info_rows[i].split())
    return info_list


def main():
    if len(sys.argv) > 1 and os.path.isdir(sys.argv[1]):

        start = time.time()
        command = 'virsh list --name'
        networks = str(subprocess.check_output(command.split()).decode("utf-8")).splitlines()
        send_to = []
        ip_info = []
        if len(networks) > 1:
            for i in range(0, len(networks) - 1):
                command = 'virsh domifaddr ' + str(networks[i])
                addresses = output(command)
                for addr in addresses:
                    ip_info.append(addr)
        for ip in ip_info:
            send_to.append(ip[3].split('/')[0])
        print(send_to)
        for ip in send_to:
            os.system("rsync -a " + sys.argv[1] + " root@" + ip + ":/tempdir")

        print(time.time() - start)


if __name__ == "__main__":
    main()

# python3 test.py /home/matija/Projects/socket-test/socket-test/data
