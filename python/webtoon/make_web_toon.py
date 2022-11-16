#!/usr/bin/env python3

import os

fp = open("index.html", "w")

files = os.listdir(".")
files.sort()

for file in files:
    print("filename :", file)
    if file[-4:] == ".png":
        fp.write("<img width=100% src={}\n><br>".format(file))

fp.close()
