# Write a Python program to create a new empty set.

x =set()
print(x)

n = set([0, 1, 2, 3, 4])
print(n)

# Write a Python program to iteration over sets.
num_set = set([0, 1, 2, 3, 4, 5])
for n in num_set:
    print(n)



# Write a Python program to add member(s) in a set.
color_set = set()
color_set.add("Red")
print(color_set)
color_set.update(["Blue","Green"])
print(color_set)



# Write a Python program to remove item(s) from set.
num_set = set([0, 1, 3, 4, 5])
num_set.pop()
print(num_set)
num_set.pop()
print(num_set)


# Write a Python program to create an intersection of sets.
#Intersection
setx = set(["green", "blue"])
sety = set(["blue", "yellow"])
setz = setx & sety
print(setz)


# Write a Python program to create a union of sets.

seta = setx | sety
print(seta)

# Write a Python program to create set difference.
setn = setx - sety
print(setn)

# Write a Python program to create a symmetric difference.
seto = setx^sety
print(setn)


# Write a Python program to test whether every element in s is in t and every element in t is in s.
setz = set(["mango"])
issubset = setx <= sety
print(issubset)
issuperset = setx >= sety
print(issuperset)
issubset = setz <= sety
print(issubset)
issuperset = sety >= setz
print(issuperset)


# Write a Python program to create a shallow copy of sets.
setp = set(["Red", "Green"])
setq = set(["Green", "Red"])
#A shallow copy
setr = setp.copy()
print(setr)


# Write a Python program to clear a set.
setq.clear()
print(setq)

# Write a Python program to use of frozensets.

x = frozenset([1, 2, 3, 4, 5])
y = frozenset([3, 4, 5, 6, 7])
#use isdisjoint(). Return True if the set has no elements in common with other.
print(x.isdisjoint(y))
#use difference(). Return a new set with elements in the set that are not in the others.
print(x.difference(y))
#new set with elements from both x and y
print(x | y)


# Write a Python program to find maximum and the minimum value in a set.
#Create a set
seta = set([5, 10, 3, 15, 2, 20])
#Find maximum value
print(max(seta))
#Find minimum value
print(min(seta))
