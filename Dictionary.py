# Write a Python program to add a key to a dictionary.

d = {0:10, 1:20}
print(d)
d.update({2:30})
print(d)

# Write a Python program to sum all the items in a dictionary.
my_dict = {'data1':100,'data2':-54,'data3':247}
print(sum(my_dict.values()))

# Write a Python program to multiply all the items in a dictionary.

my_dict = {'data1':100,'data2':-54,'data3':247}
result =1
for key in my_dict:
    result = result * my_dict[key]

print(result)

# Write a Python program to remove a key from a dictionary.

myDict = {'a':1,'b':2,'c':3,'d':4}
print(myDict)
if 'a' in myDict:
    del myDict['a']
print(myDict)

# Write a Python program to map two lists into a dictionary.

keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
color_dictionary = dict(zip(keys, values))
print(color_dictionary)


# Write a Python program to sort a dictionary by key.

color_dict = {'red': '#FF0000',
              'green': '#008000',
              'black': '#000000',
              'white': '#FFFFFF'}

for key in sorted(color_dict):
    print("%s: %s" % (key, color_dict[key]))

# Write a Python program to get the maximum and minimum value in a dictionary.

my_dict = {'x':500, 'y':5874, 'z': 560}

key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))

print('Maximum Value: ',my_dict[key_max])
print('Minimum Value: ',my_dict[key_min])

# Write a Python program to remove duplicates from Dictionary.
student_data = {'id1':
   {'name': ['Sara'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
 'id2':
  {'name': ['David'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
 'id3':
    {'name': ['Sara'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
 'id4':
   {'name': ['Surya'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
}

result = {}

for key,value in student_data.items():
    if value not in result.values():
        result[key] = value

print(result)

# Write a Python program to get a dictionary from an object's fields.

class dictObj(object):
    def __init__(self):
        self.x = 'red'
        self.y = 'yellow'
        self.z = 'Green'

    def do_nothing(self):
        pass

test = dictObj()
print(test.__dict__)


# Write a Python program to check a dictionary is empty or not.
my_dict = {}

if not bool (my_dict):
    print('Dictionary is empty')

# Write a Python program to combine two dictionary adding values for common keys.
from collections import Counter
d1 = {'a':100,'b':200,'c':300}
d2 = {'a':300, 'b':400,'c':600}

d = Counter(d1) + Counter(d2)
print(d)

# Write a Python program to print all unique values in a dictionary.
L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
print("Original List: ",L)
u_value = set( val for dic in L for val in dic.values())
print("Unique Values: ",u_value)

# Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.
import itertools

d = {'1': ['a', 'b'], '2': ['c', 'd']}
for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
    print(''.join(combo))

# Write a Python program to find the highest 3 values in a dictionary.

from heapq import nlargest
my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
three_largest = nlargest(3, my_dict, key=my_dict.get)
print(three_largest)


# Write a Python program to combine values in python list of dictionaries.

from collections import Counter
item_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
result = Counter()
for d in item_list:
    result[d['item']] += d['amount']
print(result)

# Write a Python program to create a dictionary from a string.
from collections import  defaultdict, Counter
str1 = 'w3resource'
my_dict = {}
for letter in str1:
    my_dict[letter] = my_dict.get(letter, 0) + 1
print(my_dict)

# Write a Python program to print a dictionary in table format.

my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
for row in zip(*([key] + (value) for key, value in sorted(my_dict.items()))):
    print(*row)

# Write a Python program to count the values associated with key in a dictionary.
student = [{'id': 1, 'success': True, 'name': 'Lary'},
 {'id': 2, 'success': False, 'name': 'Rabi'},
 {'id': 3, 'success': True, 'name': 'Alex'}]
print(sum(d['success'] for d in student))


# Write a Python program to convert a list into a nested dictionary of keys.

num_list = [1, 2, 3, 4]
new_dict = current = {}
for name in num_list:
    current[name] = {}
    current = current[name]
print(new_dict)


# Write a Python program to sort a list alphabetically in a dictionary.

num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
sorted_dict = {x: sorted(y) for x,y in num.items()}
print(sorted_dict)

# Write a Python program to remove spaces from dictionary keys
# .
student_list = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
print("Original dictionary: ",student_list)
studrnt_dict = {x.translate({32: None}): y for x,y in student_list.items()}
print("New Dictionary: ",studrnt_dict)

# Write a Python program to get the top three items in a shop.
from heapq import  nlargest
from operator import  itemgetter

items = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}

for name, value in nlargest(3, items.items(), key=itemgetter(1)):
    print(name,value)


# Write a Python program to get the key, value and item in a dictionary.
dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print("key  value  count")
for count, (key, value) in enumerate(dict_num.items(), 1):
    print(key,'   ',value,'    ', count)


# Write a Python program to print a dictionary line by line.

students = {'Aex': {'class': 'V',
                    'rolld_id': 2},
            'Puja': {'class': 'V',
                     'roll_id': 3}}
for a in students:
    print(a)
    for b in students[a]:
        print(b, ':', students[a][b])

# Write a Python program to check multiple keys exists in a dictionary.

student = {
  'name': 'Alex',
  'class': 'V',
  'roll_id': '2'
}
print(student.keys() >= {'class', 'name'})
print(student.keys() >= {'name', 'Alex'})
print(student.keys() >= {'roll_id', 'name'})


# Write a Python program to count number of items in a dictionary value that is a list.
dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}

ctr = sum(map(len, dict.values()))
print(ctr)

# Write a Python program to sort Counter by value.
from collections import  Counter
x = Counter({'Math':81, 'Physics':83, 'Chemistry':87})
print(x.most_common())

# Write a Python program to create a dictionary from two lists without losing duplicate values.

from collections import defaultdict
class_list = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
id_list = [1, 2, 2, 3]
temp = defaultdict(set)
for c, i in zip(class_list, id_list):
    temp[c].add(i)
print(temp)

# Write a Python program to replace dictionary values with their sum.

def sum_math_v_vi_average(list_of_dicts):
    for d in list_of_dicts:
        n1 = d.pop('V')
        n2 = d.pop('VI')
        d['V+VI'] = (n1 + n2)/2
    return list_of_dicts
student_details= [
  {'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82},
  {'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},
  {'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}
]
print(sum_math_v_vi_average(student_details))

# Write a Python program to match key values in two dictionaries.
x = {'key1': 1, 'key2': 3, 'key3': 2}
y = {'key1': 1, 'key2': 2}

for (key, value) in set(x.items()) & set(y.items()):
    print('%s: %s is present in both x and y' % (key, value))