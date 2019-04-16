# Write a Python program to create an array of 5 integers and display the array items. Access individual element through indexes.

from array import *
array_num = array('i', [1,2,3,4,5,6,7,8,9])
for i in array_num:
    print(i)
print('Access First three items individually')
print(array_num[0])
print(array_num[3])
print(array_num[5])

# Write a Python program to append a new item to the end of the array.
print("After Aooend the data")
array_num.append(11)
print("new Array: "+str(array_num))

# Write a Python program to reverse the order of the items in the array.
array_num.reverse()
print("After Reverse : "+str(array_num))


# Write a Python program to get the length in bytes of one array item in the internal representation.
print("Length in bytes of one array itme: "+str(array_num.itemsize))


# Write a Python program to get the current memory address and the length in elements of the buffer used to hold an array’s contents and also find the size of the memory buffer in bytes.

print("Original array: "+str(array_num))
print("Current memory address and the length in elements of the buffer: "+str(array_num.buffer_info()))
print("The size of the memory buffer in bytes: "+str(array_num.buffer_info()[1] * array_num.itemsize))


# Write a Python program to get the number of occurrences of a specified element in an array.
print("Number of occurrences of the number 3 in the said array: "+str(array_num.count(3)))


# Write a Python program to convert an array to an array of machine values and return the bytes representation.
print("Bytes to String: ")
x = array('b', [119, 51, 114, 101,  115, 111, 117, 114, 99, 101])
s = x.tobytes()
print(s)


# Write a Python program to append items from a specified list.


num_list = [1, 2, 6, -8]
array_num = array('i', [])
print("Items in the list: " + str(num_list))
print("Append items from the list: ")
array_num.fromlist(num_list)
print("Items in the array: "+str(array_num))



# Write a Python program to insert a new item before the second element in an existing array.
print("Original array: "+str(array_num))
print("Insert new value 4 before 3:")
array_num.insert(1, 4)
print("New array: "+str(array_num))


# Write a Python program to convert an array to an ordinary list with the same items.
array_num = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
print("Original array: "+str(array_num))
num_list = array_num.tolist()
print("Convert the said array to an ordinary list with the same items:")
print(num_list)