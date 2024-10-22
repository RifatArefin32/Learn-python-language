# Creating a set
my_set = {1, 2, 3, 4}

# Duplicate values are automatically removed and they are kept in sorted order
my_set = {23, 1, 2, 2, 3}
print(my_set)  # Output: {1, 2, 3}

# Using the set() constructor to create a set from a list
another_set = set([1, 2, 3, 3, 4])
print(another_set)  # Output: {1, 2, 3, 4}

# Add an element in a set
my_set.add(444)
print(my_set)   # Output: {1, 2, 3, 23, 444}

# Remove an element from the set
my_set.remove(444)
print(my_set)   # Output: {1, 2, 3, 23}

# See if an item
print(444 in my_set)

# Add touple at set
my_set.add((45, "mango"))
print(my_set)

# Add touple at set
my_set.add((45, "mango", "orange"))
print(my_set)

# Union, intersection, difference
set_1 = {1, 2, 4, 6}
set_2 = {3, 6, 7}

print("Set_1: ", set_1)
print("Set_2: ", set_2)

union = set_1.union(set_2) 
print("Union: ", union)

union = set_1.intersection(set_2) 
print("Interaction: ", union)

union = set_1.difference(set_2) 
print("Difference: ", union)