import paramiko

with open("pw", 'r') as passFile:
    pw = passFile.readline()
ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname='10.18.110.49', port=22, username='root',
            password=pw, timeout=3)

stdin, stdout, stderr = ssh.exec_command('mkdir -p /home/matija/paramiko5')
# stdin, stdout, stderr = ssh.exec_command('cd paramiko5')
stdin, stdout, stderr = ssh.exec_command("cd /home/matija/paramiko5 \n echo '555' >> /home/matija/paramiko5/pFile")

ftp_client = ssh.open_sftp()
ftp_client.put('/home/matija/Projects/socket-test/socket-test/data/big', '/home/matija/paramiko/big2')
ftp_client.close()
