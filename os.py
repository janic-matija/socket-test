import os
import subprocess
import time
import xml.etree.ElementTree as ET


def main():
    command = 'virsh list --name'
    data = []
    vms = str(subprocess.check_output(command.split()).decode("utf-8")).splitlines()
    print(vms)
    for i in range(0, len(vms) - 1):
        command = "sudo virt-inspector -d " + vms[i]
        data = ET.parse(subprocess.check_output(command.split())[0:700])
        # data = str(subprocess.check_output(command.split()).decode("utf-8"))[0:700]  # .splitlines()
        nesto = data.getroot().tag
        # data = data[data.index('<osinfo>') + len('<osinfo>'): data.index('</osinfo>')]
        print(nesto)
        if 'win' in data:
            data = 'windows'
        elif 'ubuntu' in data:
            data = 'ubuntu'

        # print(data)


if __name__ == "__main__":
    start = time.time()
    main()
    print(time.time() - start)
