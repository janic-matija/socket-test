import fabric

with open("pw", 'r') as passFile:
    password = passFile.readline()

c = fabric.Connection("10.18.110.49", port=22, user="root", connect_kwargs={'password': password})

c.run("mkdir -p fabric35")
c.run("cd fabric35 \n echo 'fabricTest' >> ftFile")
