# write a Python program to check whether a file exists

import os
open('abc.txt','r')
print(os.path.isfile('abc.txt'))

# Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on os

import struct
print(struct.calcsize("P")*8)

#get os name , Platform and release information

# import os
import platform
print(os.name)
print(platform.system())
print(platform.machine())
print(platform.processor())
print(platform.release())


# Write a python program to list all files in a directory in python

from os import  listdir
from os.path import  isfile, join

files_list = []
for f in listdir('C:\Users\Administrator\Downloads\Video'):
    files_list.append(f)
print(files_list);