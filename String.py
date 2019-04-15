# Calculate the length of a string

def string_length(str1):
    count = 0
    for char in str1:
        count +=1
    return  count
print(string_length('My Name is Khan'))

# Count the number of characters(character frequency) in a string

def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] +=1
        else:
            dict[n] =1
    return dict

print(char_frequency('google.com'))


def change_char(str1):
  char = str1[0]
  str1 = str1.replace(char, '$')
  str1 = char + str1[1:]

  return str1

print(change_char('restart'))


def chars_mix_up(a, b):
  new_a = b[:2] + a[2:]
  new_b = a[:2] + b[2:]

  return new_a + ' ' + new_b
print(chars_mix_up('abc', 'xyz'))


def add_string(str1):
  length = len(str1)

  if length > 2:
    if str1[-3:] == 'ing':
      str1 += 'ly'
    else:
      str1 += 'ing'

  return str1
print(add_string('ab'))
print(add_string('abc'))
print(add_string('string'))


def not_poor(str1):
    snot = str1.find('not')
    spoor = str1.find('poor')

    if spoor > snot and snot > 0 and spoor > 0:
        str1 = str1.replace(str1[snot:(spoor + 4)], 'good')
        return str1
    else:
        return str1


print(not_poor('The lyrics is not that poor!'))
print(not_poor('The lyrics is poor!'))



# def find_longest_word(words_list):
#     words_len = []
#     for n in words_list:
#         words_len.append(len(n),n)
#
#     words_len.sort()
#     return words_len[-1][1]
#
# print(find_longest_word(["PHP", "Exercises", "Backend"]))


def remove_char(str, n):
    first_part = str[:n]
    last_part = str[n + 1:]
    return first_part + last_part


print(remove_char('Python', 0))
print(remove_char('Python', 3))
print(remove_char('Python', 5))


def change_sring(str1):
    return str1[-1:] + str1[1:-1] + str1[:1]


print(change_sring('abcd'))
print(change_sring('12345'))


def odd_values_string(str):
  result = ""
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result

print(odd_values_string('abcdef'))
print(odd_values_string('python'))




def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print( word_count('the quick brown fox jumps over the lazy dog.'))



def insert_end(str):
    sub_str = str[-2:]
    return  sub_str * 4

print(insert_end('Python'))
print(insert_end('Execises'))


def first_three(str):
    return str[:3] if len(str) > 3 else str

print(first_three('natokpy'))
print(first_three('python'))
print(first_three('py'))


def reverse_string(str1):
    if len(str1) % 4 == 0:
       return ''.join(reversed(str1))
    return str1

print(reverse_string('abcd'))
print(reverse_string('python'))


# def lexicographi_sort(s):
#     print(sorted(s))
#
#     return  sorted(sorted(s), key=str.upper())
#
# lexicographi_sort('w3resource')
# print(lexicographi_sort('quickbrown'))


# def to_uppercase(str1):
#     num_upper = 0
#     for letter in str1[:4]:
#         if letter.upper() == letter:
#             num_upper += 1
#     if num_upper >= 2:
#         return str1.upper()
#     return str1
#
# print(to_uppercase('Python'))
# print(to_uppercase('PyThon'))


string = "w3resource.com"
print(string.startswith("w3r"))


# https://gist.github.com/nchitalov/2f2b03e5cf1e19da1525
def caesar_encrypt(realText, step):
    outText = []
    cryptText = []

    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']

    for eachLetter in realText:
        if eachLetter in uppercase:
            index = uppercase.index(eachLetter)
            crypting = (index + step) % 26
            cryptText.append(crypting)
            newLetter = uppercase[crypting]
            outText.append(newLetter)
        elif eachLetter in lowercase:
            index = lowercase.index(eachLetter)
            crypting = (index + step) % 26
            cryptText.append(crypting)
            newLetter = lowercase[crypting]
            outText.append(newLetter)
    return outText


code = caesar_encrypt('abc', 2)
print()
print(code)
print()



import textwrap
sample_text = '''
  Python is a widely used high-level, general-purpose, interpreted,
  dynamic programming language. Its design philosophy emphasizes
  code readability, and its syntax allows programmers to express
  concepts in fewer lines of code than possible in languages such
  as C++ or Java.
  '''
print()
print(textwrap.fill(sample_text, width=50))
print()


x = 3
y = 123
print("\nOriginal Number: ", x)
print("Formatted Number(right padding, width 2): "+"{:*< 3d}".format(x));
print("Formatted Number(right padding, width 2): "+"{:0>3d}".format(x));
print("Original Number: ", y)
print("Formatted Number(right padding, width 6): "+"{:*< 7d}".format(y));
print("Formatted Number(right padding, width 6): "+"{:0>7d}".format(y));
print()
print("\nOriginal Number: ", x)
print("Left aligned (width 10)   :"+"{:< 10d}".format(x));
print("Right aligned (width 10)  :"+"{:10d}".format(x));
print("Center aligned (width 10) :"+"{:^10d}".format(x));
print()




import collections
str1 = 'thequickbrownfoxjumpsoverthelazydog'
d = collections.defaultdict(int)
for c in str1:
    d[c] += 1

for c in sorted(d, key=d.get, reverse=True):
  if d[c] > 1:
      print('%s %d' % (c, d[c]))


str1 ="w3resource"

for index, char in enumerate(str1):
    print("Current character", char , "position st", index)


    def first_non_repeating_character(str1):
        char_order = []
        ctr = {}
        for c in str1:
            if c in ctr:
                ctr[c] += 1
            else:
                ctr[c] = 1
                char_order.append(c)
        for c in char_order:
            if ctr[c] == 1:
                return c
        return None


    print(first_non_repeating_character('abcdef'))
    print(first_non_repeating_character('abcabcdef'))
    print(first_non_repeating_character('aabbcc'))


def first_repeated_char(str1):
  for index,c in enumerate(str1):
    if str1[:index+1].count(c) > 1:
      return c
  return "None"

print(first_repeated_char("abcdabcd"))
print(first_repeated_char("abcd"))


def move_Spaces_front(str1):
  noSpaces_char = [ch for ch in str1 if ch!=' ']
  spaces_char = len(str1) - len(noSpaces_char)
  result = ' '*spaces_char
  result = '"'+result + ''.join(noSpaces_char)+'"'
  return(result)

print(move_Spaces_front("w3resource .  com  "))
print(move_Spaces_front("   w3resource.com  "))


def remove_zeros_from_ip(ip_add):
  new_ip_add = ".".join([str(int(i)) for i in ip_add.split(".")])
  return new_ip_add ;

print(remove_zeros_from_ip("255.024.01.01"))
print(remove_zeros_from_ip("127.0.0.01 "))

from itertools import groupby


def remove_all_consecutive(str1):
    result_str = []
    for (key, group) in groupby(str1):
        result_str.append(key)

    return ''.join(result_str)


str1 = 'xxxxxyyyyy'
print("Original string:" + str1)
print("After removing consecutive duplicates: " + str1)
print(remove_all_consecutive(str1))




from collections import Counter
def generateStrings(input):
     str_char_ctr = Counter(input)
     part1 = [ key for (key,count) in str_char_ctr.items() if count==1]
     part2 = [ key for (key,count) in str_char_ctr.items() if count>1]
     part1.sort()
     part2.sort()
     return part1,part2
input = "aabbcceffgh"
s1, s2 = generateStrings(input)
print(''.join(s1))
print(''.join(s2))
