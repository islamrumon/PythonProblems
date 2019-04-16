# Write a Python program to create a tuple with different data types.

tuples = ("tuple", False, 3.2,1)
print(tuples)

# Write a Python program to create a tuple.
x = ()
print(x)

tuples = tuple()
print(tuples)

# Write a Python program to create a tuple with numbers and print one item.
tuplex = 5,10,15,20,25
print(tuplex)

tuplex =5,
print(tuplex)


# Write a Python program to unpack a tuple in several variables.
#create a tuple
tuplex = 4, 8, 3
print(tuplex)
n1, n2, n3 = tuplex
#unpack a tuple in variables
print(n1 + n2 + n3)
#the number of variables must be equal to the number of items of the tuple


# Write a Python program to add an item in a tuple.
tuplex = (4,6,2,8,3,1)
print(tuplex)

tuplex = tuplex + (9,)
tuplex = tuplex[:5] + (15, 20, 25) + tuplex[:5]
print(tuplex)

listx = list(tuplex)
listx.append((30))
tuplex = tuple(listx)
print(tuplex)


# Write a Python program to convert a tuple to a string.
tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
str =  ''.join(tup)
print(str)


# Write a Python program to get the 4th element and 4th element from last of a tuple.

tuplex = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
print(tuplex)
item = tuplex[3]
print(item)

item1 = tuplex[-4]
print(item1)

# Write a Python program to create the colon of a tuple.
from copy import deepcopy
tuplex = ("HELLO", 5, [], True)
print(tuplex)
tuplex_colon = deepcopy(tuplex)
tuplex_colon[2].append(50)
print(tuplex_colon)
print(tuplex)

# Write a Python program to find the repeated items of a tuple
tuplex = 2, 4, 5, 6, 2, 3, 4, 4, 7
print(tuplex)
count = tuplex.count(4)
print(count)

# Write a Python program to check whether an element exists within a tuple.
tuplex = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
print("r" in tuplex)
print(5 in tuplex)


# Write a Python program to convert a list to a tuple.
#Convert list to tuple
listx = [5, 10, 7, 4, 15, 3]
print(listx)
tuplex = tuple(listx)
print(tuplex)

# Write a Python program to remove an item from a tuple.
#create a tuple
tuplex = "w", 3, "r", "s", "o", "u", "r", "c", "e"
print(tuplex)
print(tuplex[:2])
print(tuplex[3:])
tuplex = tuplex[:2] + tuplex[3:]
print(tuplex)
listx = list(tuplex)
listx.remove("c")
tuplex = tuple(listx)
print(tuplex)

# Write a Python program to slice a tuple.

tuplex = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)

_slice = tuplex[3:5]

print(_slice)
_slice = tuplex[:6]
print(_slice)

_slice = tuplex[5:]
print(_slice)

_slice = tuplex[:]
print(_slice)
_slice = tuplex[-8:-4]
print(_slice)
tuplex = tuple("HELLO WORLD")
print(tuplex)
_slice = tuplex[2:9:2]
print(_slice)
_slice = tuplex[::4]
print(_slice)
_slice = tuplex[9:2:-4]
print(_slice)



# Write a Python program to convert a tuple to a dictionary.
#create a tuple
tuplex = ((2, "w"),(3, "r"))
print(dict((y, x) for x, y in tuplex))


# Write a Python program to convert a list of tuples into a dictionary.
l = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]

d = {}
for a,b in l:
    d.setdefault(a,[]).append(b)
print(d)


# Write a Python program to print a tuple with string formatting.
t = (100, 200, 300)
print('This is a tuple {0}'.format(t))


# Write a Python program to replace last value of tuples in a list.
l = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print([t[:-1] + (100,) for t in l])


# Write a Python program to remove an empty tuple(s) from a list of tuples.

L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
L = [t for t in L if t]
print(L)


# Write a Python program to sort a tuple by its float element.
price = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
print( sorted(price, key=lambda x: float(x[1]), reverse=True))


# Write a Python program to count the elements in a list until an element is a tuple.

num = [10,20,30,(10,20),40]
ctr = 0
for n in num:
    if isinstance(n, tuple):
        break
    ctr += 1
print(ctr)
