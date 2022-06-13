import os

#import the shutil module
import shutil

#write the path of the file
path=r'I:\linux_work\python_automation\os_library\folder1'

#List all the files and directories in the file path

print("Before copying file:")
print(os.listdir(path))

#write the source path
source=path+'/text1.txt'
print(source)
#print the file permission of the source
perms=os.stat(source).st_mode
print("File Permission mode:",perms,"\n")

dest=r'I:\linux_work\python_automation\os_library\folder1\destination'
#copy the content of source file to destination
dests=shutil.copy(source,dest)

#List files and directories of the path
print("After copying file:")
print(os.listdir(dest))

#print again all permissions
perms=os.stat(dest).st_mode
print("File Permission Mode:",perms)