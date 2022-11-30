import platform

print(platform.uname().system)
if platform.uname().system == 'Windows':
    folder = 'C:/ProgramData/tempdir/data'
elif platform.uname().system == 'Ubuntu':
    folder = '/tempdir/data'
