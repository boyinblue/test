import os

def openFile(filename):
    fp = open("~/{}".format(filename))
    line = fp.readline()
    print(line)

def openFileByFullPath(full_path):
    fp = open(full_path)
    line = fp.readline()
    print(line)

def openFile2(filename):
    home_dir = os.path.expanduser('~')
    fp = open("{}/{}".format(home_dir, filename))
    line = fp.readline()
    print(line)

#openFile(".git-credentials")
openFileByFullPath("/home/parksejin/.git-credentials")
openFile2(".git-credentials")
