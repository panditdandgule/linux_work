import os

print("Current Working directory:",os.getcwd())
print("Getting the status of the file:",os.stat('allinone.py'))
print("Execute Shell command:",os.system('dir -f'))
print("Return the current process Id:",os.getpid())
#print("Change permission mode:",os.chmod())#os.chmod(path, mode)
#os.chown(path, uid, gid)

print("Check if a path exists with :",os.path.exists('file1.txt'))
#print("Create new directory:",os.mkdir('folder1'))

def check_all():
    os.mkdir('./tmp')
    if os.path.isdir('./python_automation') or  os.path.isfile('file1.txt'):
        print("Its directory or file")
    elif os.walk():
        for root, dirs, files in os.walk("/tmp"):
            print(root)
            print(dirs)
            print(files)
    elif os.path.getatime('/tmp'):
        print("Get the last time a directory was accessed with ")

        # Get the user ID with os.getuid()
    elif os.getuid() != 0:
        print("you are not root")

        # Get the group ID with os.getgid()
        print(os.getgid())

        # Return the name of the user logged in with os.getlogin()
        print(os.getlogin())

        # Returns a list of all files in a directory with os.listdir()
        for filename in os.listdir("/tmp"):
            print("This is inside /tmp", filename)

        # Get the size of a file with os.path.getsize()
        #path.getsize("/tmp/file.txt")


