import os
import subprocess
import time


def main():
    command = 'virsh list --name'
    data = []
    vms = str(subprocess.check_output(command.split()).decode("utf-8")).splitlines()
    print(vms)
    for i in range(0, len(vms) - 1):
        command = "sudo virt-inspector -d " + vms[i]
        data = (str(subprocess.check_output(command.split())[0:700].decode("utf-8"))[0:700]).splitlines()
        osinfo = ''
        for tag in data:
            if '<osinfo>' in tag:
                osinfo = tag[tag.index('<osinfo>') + len('<osinfo>'): tag.index('</osinfo>')]
        if 'win' in osinfo:
            osinfo = 'windows'
        elif 'ubuntu' in osinfo:
            osinfo = 'ubuntu'

        print(osinfo)


if __name__ == "__main__":
    main()

