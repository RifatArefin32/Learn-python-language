# Creating a dictionary
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}

print(my_dict["name"])  # Output: Alice
print(my_dict["age"])   # Output: 30

my_dict["email"] = "alice@example.com"  # Adding a new key-value pair
my_dict["age"] = 31  # Updating an existing key's value

print(my_dict) # Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'email': 'alice@example.com'}

del my_dict["city"]  # Remove using del
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'email': 'alice@example.com'}

# Using pop() to remove and return a value
email = my_dict.pop("email")
print(email)  # Output: alice@example.com
print(my_dict)


print(my_dict.get("name"))  # Output: Alice
print(my_dict.get("address", "Not found"))  # Output: Not found

print(my_dict.keys())  # Output: dict_keys(['name', 'age'])
print(my_dict.values())  # Output: dict_values(['Alice', 31])
print(my_dict.items())  # Output: dict_items([('name', 'Alice'), ('age', 31)])


# Looping over keys
for key in my_dict:
    print(key)

# Looping over values
for value in my_dict.values():
    print(value)

# Looping over key-value pairs
for key, value in my_dict.items():
    print(f"{key}: {value}")


if "name" in my_dict:
    print("Name is present")

