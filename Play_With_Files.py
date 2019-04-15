# this code for right some text

# with open('abc.txt', 'w') as f:
#     data = 'Python has several built-in modules and functions for handling files. These functions are spread out over several modules such as os, os.path, shutil, and pathlib, to name a few. This article gathers in one place many of the functions you need to know in order to perform the most common operations on files in Python.'
#     f.write(data)

# this code fro read txt filr
# with open('abc.txt','r') as f:
#     data = f.read()
#     print(data)


# print all file from directory
import  os
with os.scandir('C:/Users/Administrator/Downloads/Video/') as entries:
    for entry in entries:
        print(entry.name)



# Write a Python program to determine profiling of Python programs.
import cProfile
def sum():
    print(1+2)
cProfile.run('sum()')


# Write a python program to access environment variables.
import  os
print(os.environ)

# Write a Python program to get the current username.
import  getpass
print(getpass.getuser())


# Write a program to get execution time (in seconds) for a Python method.
import  time
def sum_of_numbers(n):
    start_time = time.time()
    s = 0
    for i in range (1, n+1):
        s =s +i
        end_time = time.time()
        return s , end_time - start_time

n = 5
print("\nTime to sum of 1 to ",n," and required time to calculate is :",sum_of_numbers(n))

# Python: Calculate the hypotenuse of a right angled triangle
from math import  sqrt
print("Input Iengths of shorter triangle sides:")
# a = float(input("a: "))
# b = float(input("b: "))
a,b =2,5
c = sqrt(a**2 + b**2)

print("The Length is ",c)

# Write a Python program to convert the distance (in feet) to inches, yards, and miles.
# d_ft = int(input("Input distance in feet: "))
d_ft = 12
d_inches = d_ft * 12
d_yards = d_ft / 3.0
d_miles = d_ft / 5280.0

print("The distance in inches is %i inches." % d_inches)
print("The distance in yards is %.2f yards." % d_yards)
print("The distance in miles is %.2f miles." % d_miles)


# Write a Python program to get an absolute file path.
def absolute_file_path(path_fname):
    import os
    return os.path.abspath('path_fname')
print("Absolute file path: ",absolute_file_path('abc.txt'))

# Write a Python program to get the command-line arguments (name of the script, the number of arguments, arguments) passed to a script.

import sys
print("This is the name/path of the script:"),sys.argv[0]
print("Number of arguments:",len(sys.argv))
print("Argument List:",str(sys.argv))

# Write a Python program to find the available built-in modules.
import sys
import textwrap
module_name = ', '.join(sorted(sys.builtin_module_names))
print(textwrap.fill(module_name, width= 70))

import os
file_size = os.path.getsize("abc.txt")
print("\n The Size of abc.txt", file_size)

a = 30
b = 20
print("\nBefore swap a = %d and b = %d" %(a, b))
a, b = b, a
print("\nAfter swaping a = %d and b = %d" %(a, b))
print()

# Write a Python program to get the identity of an object.
obj1 = object()
obj1_address = id(obj1)
print(obj1_address)

def max_min(data):
  l = data[0]
  s = data[0]
  for num in data:
    if num> l:
      l = num
    elif num< s:
        s = num
  return l, s

print(max_min([0, 10, 15, 40, -5, 42, 17, 28, 75]))

# Write a Python function that takes a positive integer and returns the sum of the cube of all the positive integers smaller than the specified number.

def sum_of_cubes(n):
    n -= 1
    total = 0
    while n > 0:
        total += n*n*n
        n -=1
    return  total
print("the cubes ",sum_of_cubes(19))


def odd_product(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                product = nums[i] * nums[j]
                if product & 1:
                    return True
                    return False


dt1 = [2, 4, 6, 8]
dt2 = [1, 6, 4, 7, 8]
print(dt1, odd_product(dt1));
print(dt2, odd_product(dt2));

