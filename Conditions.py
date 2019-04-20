# Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included)
nl=[]
for x in range(1500, 2701):
    if (x%7==0) and (x%5==0):
        nl.append(str(x))
print(','.join(nl))


# Write a Python program to convert temperatures to and from celsius, fahrenheit.
# temp = input("Input the  temperature you like to convert? (e.g., 45F, 102C etc.) : ")
temp = "34C"
degree = int(temp[:-1])
print(degree)
i_convention = temp[-1]

if i_convention.upper() == "C":
  result = int(round((9 * degree) / 5 + 32))
  o_convention = "Fahrenheit"
elif i_convention.upper() == "F":
  result = int(round((degree - 32) * 5 / 9))
  o_convention = "Celsius"
else:
  print("Input proper convention.")
  quit()
print("The temperature in", o_convention, "is", result, "degrees.")

# Write a Python program to guess a number between 1 to 9.
# Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.

import random
target_num, guess_num = random.randint(1,10),0
print(target_num)
while target_num != guess_num:
     guess_num = int(input('Guess a number between 1 and 10 until you get it right : '))
print('Well guessed!')


# Write a Python program to construct the following pattern, using a nested for loop.
n =5
for i in range(n):
    for j in range(i):
        print('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')


# Write a Python program that accepts a word from the user and reverse it.

word = input("Input a word to reverse: ")
print(len(word) -1,-1,-1)
for char in range(len(word) -1,-1,-1):
    print(word[char], end="")
print("\n")


# Write a Python program to count the number of even and odd numbers from a series of numbers.
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the tuple
count_odd = 0
count_even = 0
for x in numbers:
        if not x % 2:
    	     count_even+=1
        else:
    	     count_odd+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)

# Write a Python program that prints each item and its corresponding type from the following list.

datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12],
{"class":'V', "section":'A'}]

for item in datalist:
    print("Type of",item,"is", type(item))

# Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
for x in range(6):
    if (x == 3 or x == 6):
        continue
    print(x,end=' ')
print("\n")


# Write a Python program to get the Fibonacci series between 0 to 50.
x,y =0,1

while y < 50:
    print(y)
    x,y = y, x+y


# Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

for fizzbuzz in range(50):
    if fizzbuzz % 3 == 0 and fizzbuzz %5 ==0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print('fizz')
        continue
    elif fizzbuzz % 5 == 0:
        print('buzz')
        continue
    print(fizzbuzz)

# Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
# Note :
# i = 0,1.., m-1
# j = 0,1, n-1.


row_num = int(input("Input number of rows: "))
col_num = int(input("Input number of columns: "))
multi_list = [[0 for col in range(col_num)] for row in range(row_num)]
print(multi_list)
for row in range(row_num):
    for col in range(col_num):
        multi_list[row][col]= row*col

print(multi_list)


# Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lower case).
lines = []
while True:
    l = input()
    if l:
        lines.append(l.upper())
    else:
        break;
for l in lines:
    print(l)

# Write a Python program which accepts a sequence of comma separated 4 digit binary numbers as its input and print the numbers that are divisible by 5 in a comma separated sequence.
items = []
num = [x for x in input().split(',')]

for p in num:
    x = int(p,2)
    if not x % 5:
        items.append(p)
print(','.join(items))


# Write a Python program that accepts a string and calculate the number of digits and letters.

s = input("Input a string")
d=l=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("Letters", l)
print("Digits", d)


# Write a Python program to check the validity of a password (input from users).
#
# Validation :
#
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.


import  re
p = input("Input your password")
x = True
while x:
    if(len(p)<6 or len(p) > 12):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]", p):
        break
    elif not re.search("[A-Z]", p):
        break
    elif not re.search("[$#@]", p):
        break
    elif re.search("\s", p):
        break
    else:
        print("Valid Password")
        x = False
        break

if x:
 print("Not a Valid Password")


items = []
for i in range(100, 401):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0):
        items.append(s)
print( ",".join(items))

# Write a Python program to print alphabet pattern 'A'.

rsult_str="";
for row in range(0,7):
    for col in range(0,7):
        if(((col == 1 or col == 5) and row != 0 )or ((row ==0 or row == 3) and (col > 1 and col < 5))):
            result_str = result_str + "*"
        else:
            result_str = result_str + " "
    result_str = result_str + "\n"
print(result_str);


