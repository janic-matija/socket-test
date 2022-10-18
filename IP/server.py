import paramiko


ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname='10.18.110.49', port=22, username='root',
            password='Baccano!13', timeout=3)

stdin, stdout, stderr = ssh.exec_command('mkdir paramiko')
