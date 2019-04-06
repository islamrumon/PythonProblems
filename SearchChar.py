def is_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels

print(is_vowel('c'))
print(is_vowel('e'))


#p-25
def is_group_member(group_data , n):
    for value in group_data:
        if n == value:
            return True
    return False


print(is_group_member([1,5,8,3],5))
print(is_group_member([5,8,3],-1))

#p-26
def histogram(items):
    for n in items:
        output = ''
        time = n
        while (time > 0):
            output += '*'
            time = time - 1
        print(output)

histogram([2,3,6,5])


#p-27

def concatenate_list_data(list):
    result = ''
    for n in list:
        result += str(n)

    return result;

print(concatenate_list_data([1,4,72,9,0]))
