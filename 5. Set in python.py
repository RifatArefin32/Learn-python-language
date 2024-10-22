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

