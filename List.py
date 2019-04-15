# Sum all the items in a list

def sum_list(items):
    sum_number = 0
    for x in items:
        sum_number +=x
    return sum_number
print(sum_list([1,2,-8,-9]))


# Get the largest number from a list

def max_num_in_list(list):
    max = list[0]
    for a in list:
        if a < max:
            max = a
    return max
print(max_num_in_list([1,23,34,-78]))


# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.

def match_words(words):
    ctr  = 0
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr +=1
    return ctr

print(match_words(['abc', 'xyz','1234', 'aba', '1221']))



# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples

def last(n): return n[-1]

def sort_list_last(tuples):
  return sorted(tuples, key=last)

print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))


# Write a Python program to remove duplicates from a list.
a = [10,20,30,20,10,50,60,40,80,50,40]

dup_items = set()
print(dup_items)
uniq_items = []
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)

print(dup_items)

# Write a Python program to print the numbers of a specified list after removing even numbers from it.
num = [7,8, 120, 25, 44, 20, 27]
num = [x for x in num if x%2!=0]
print(num)


# Shuffle and print a specified list
from random import shuffle
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
shuffle(color)
print(color)


# Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).

def printValues():
    l = list()
    for i in range(1,21):
        print(i)
        l.append(i**2)
    print(l)
    print(l[:5])
    print(l[-5:])

printValues()

# Write a Python program to get the difference between the two lists.

list1 = [1, 2, 3, 4]
list2 = [1, 2]
print(list(set(list1) - set(list2)))


# Write a Python program access the index of a list.
nums = [5,15,35,8,98]
for num_index, num_val in enumerate(nums):
    print(num_index, num_val)

# Write a Python program to flatten a shallow list.
import  itertools
original_list = [[2,4,3],[1,5,6], [9], [7,9,0]]
new_merged_list = list(itertools.chain(*original_list))
print(new_merged_list)


# write a Python program to append a list to the second list.
list1 = [1, 2, 3, 0]
list2 = ['Red', 'Green', 'Black']
final_list = list1 + list2
print(final_list)

# Write a Python program to select an item randomly from a list.
import random
color_list = ['Red', 'Blue', 'Green', 'White', 'Black']
print(random.choice(color_list))

# Write a python program to check whether two lists are circularly identical.
list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
list3 = [1, 10, 10, 0, 0]

print('Compare list1 and list2')
print(' '.join(map(str, list2)) in ' '.join(map(str, list1 * 2)))
print('Compare list1 and list3')
print(' '.join(map(str, list3)) in ' '.join(map(str, list1 * 2)))


# Write a Python program to find the second smallest number in a list.

def second_smallest(numbers):
  if (len(numbers)<2):
    return
  if ((len(numbers)==2)  and (numbers[0] == numbers[1]) ):
    return
  dup_items = set()
  uniq_items = []
  for x in numbers:
    if x not in dup_items:
      uniq_items.append(x)
      dup_items.add(x)
  uniq_items.sort()
  return  uniq_items[1]

print(second_smallest([1, 2, -8, -2, 0, -2]))
print(second_smallest([1, 1, 0, 0, 2, -2, -2]))
print(second_smallest([1, 1, 1, 0, 0, 0, 2, -2, -2]))
print(second_smallest([2,2]))
print(second_smallest([2]))



my_list = [10, 20, 30, 40, 20, 50, 60, 40]
print("Original List : ",my_list)
my_set = set(my_list)
my_new_list = list(my_set)
print("List of unique numbers : ",my_new_list)


# Get the frequency of the elements in a list
import collections
my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]
print("Original List : ",my_list)
ctr = collections.Counter(my_list)
print("Frequency of the elements in the List : ",ctr)


# Write a Python program to count the number of elements in a list within a specified range.
def count_range_in_list(li, min, max):
	ctr = 0
	for x in li:
		if min <= x <= max:
			ctr += 1
	return ctr

list1 = [10,20,30,40,40,40,70,80,99]
print(count_range_in_list(list1, 40, 100))

list2 = ['a','b','c','d','e','f']
print(count_range_in_list(list2, 'a', 'e'))

# Write a Python program to generate all sublists of a list.
def sub_lists(my_list):
    subs = [[]]
    for i in range(len(my_list)):
        n = i + 1
        while n <= len(my_list):
            sub = my_list[i:n]
            subs.append(sub)
            n += 1

    return subs


l1 = [10, 20, 30, 40]
l2 = ['X', 'Y', 'Z']
print(sub_lists(l1))
print(sub_lists(l2))

# Write a Python program to create a list by concatenating a given list which range goes from 1 to n.
my_list = ['p','q']
n = 4
new_list = ['{}{}'.format(x,y) for  y in range(1, n+1) for x in my_list]
print(new_list)

x = 100
print(format(id(x), 'x'))
s = 'w3resource'
print(format(id(s), 'x'))


# Write a Python program to find common items from two lists.
color1 = "Red", "Green", "Orange", "White"
color2 = "Black", "Green", "White", "Pink"
print(set(color1) & set(color2))


# Write a Python program to change the position of every n-th value with the (n+1)th in a list.
from itertools import zip_longest, chain, tee
def replace2copy(lst):
    lst1, lst2 = tee(iter(lst), 2)
    return list(chain.from_iterable(zip_longest(lst[1::2], lst[::2])))
n = [0,1,2,3,4,5]
print(replace2copy(n))


# Write a Python program to split a list based on first character of word.
from itertools import groupby
from operator import itemgetter

word_list = ['be','have','do','say','get','make','go','know','take','see','come','think',
     'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']

for letter, words in groupby(sorted(word_list), key=itemgetter(0)):
    print(letter)
    for word in words:
        print(word)


# Write a Python program to convert a list of multiple integers into a single integer.
L = [11, 33, 50]
print("Original List: ",L)
x = int("".join(map(str, L)))
print("Single Integer: ",x)


# Write a Python program to change the position of every n-th value with the (n+1)th in a list.

from itertools import zip_longest, chain, tee
def replace2copy(lst):
    lst1, lst2 = tee(iter(lst), 2)
    return list(chain.from_iterable(zip_longest(lst[1::2], lst[::2])))
n = [0,1,2,3,4,5]
print(replace2copy(n))
