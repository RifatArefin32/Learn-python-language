
# A tuple with different data types
my_tuple = (1, "apple", 3.14)

# Accessing elements in a tuple
print("First item of the touple: ", my_tuple[0])  # Output: 1

# Tuples are immutable, so the following would cause an error:
# my_tuple[0] = 2  # Error: 'tuple' object does not support item assignment

def get_user():
    name = "Alice"
    age = 30
    return (name, age)

# Unpacking a tuple
user = get_user()
print(user)        # Output: ('Alice', 30)

# Tuple unpacking
name, age = get_user()
print(name)  # Output: Alice
print(age)   # Output: 30
