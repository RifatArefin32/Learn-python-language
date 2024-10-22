st1 = 'hello world' 
print(st1)  # hellow world

st1 = "hello world" 
print(st1)  # hellow world

st1 = '''hello world''' 
print(st1)  # hellow world

st1 = """Hello
World
    This is quote
    This is line 2""" 
print(st1)  # Print the quote

# Strings objects are modifiable but immutable
str = 'hello'
print(str)  # output: hello

str = 'world'
print(str)  # output: world

# str[0] = 'x' # This modification is not possible
# print(str)

str += ' hello' # string concatenation
print(str)  # world hello

str *= 3
print(str) # output: world helloworld helloworld hello


# String format() method
default_order = "{}, {} and {} are brothers".format('Rahim', 'karim', 'Rakib')
print(default_order)

positional_order = "{1}, {2} and {0} are brothers".format('Rahim', 'karim', 'Rakib')
print(positional_order)

keyword_order = "{i}, {j} and {k} are brothers".format(i = 'Rahim', j = 'karim', k = 'Rakib')
print(keyword_order)

# Some important function
print("HELLO WORLD".lower())
print("hello world".upper())