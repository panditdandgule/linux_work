import glob

def iterate_files(fPath):
    # use glob to get the filenames of files in the folder
    fNames=glob.glob(fPath)

    for file in fNames:
        print(file)

fPath = r'I:\linux_work\python_automation\os_library\folder1\text1.txt'
iterate_files(fPath)