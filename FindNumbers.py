# Write a Python program to add two objects if both objects are an integer type.

def add_numbers(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
         raise TypeError("Inputs must be integers")
    return a+b


print(add_numbers(10, 20))



# Write a Python program to display your details like name, age, address in three different lines.
def personal_details():
    name, age = "rumon", 19
    address = "Bangladesh , india, Napel"
    print("Name: {}\nAge:{}\nAddress: {}".format(name, age, address))
personal_details()




# Write a Python program to solve (x + y) * (x + y).
x, y = 2, 3

result = x * x + 2 * x * y + y * y
print("(({} + {}) ^ 2)={} ".format(x, y, result))


# Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).

import math
p1 = [4, 0]
p2 = [6, 6]
distance = math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))

print(distance)
