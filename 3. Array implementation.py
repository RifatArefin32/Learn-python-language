# define an array
arr = [1, 2, 3, 4, 5]
print(arr)

# accessing array element using index
print("index 0: ", arr[0])   # 
# print(arr[5])   # IndexError: list index out of range
print("index -1: ", arr[-1])
print("index -2: ", arr[-2])
print("index -5: ", arr[-5])

# Length of an array
len = len(arr)
print("Length of arr: ", len)

# define mix array 
arr2 = [1, 2, 'mango', 3]
print(arr2) # [1, 2, 'mango', 3]

# add another element to arr2
arr2.append('orange')
print(arr2) # [1, 2, 'mango', 3, 'orange']

# removing the element of index `4`
print("Before removing the 4th index: ", arr2)
del arr2[4]
print("After removing the 4th index: ", arr2) # [1, 2, 'mango', 3]
arr2.pop(1)
print("After removing the 1st index: ", arr2)

# remove an element with name 'mango'
arr2.append('mango')
print("Before removing mango: ", arr2)
arr2.remove('mango')    # remove first `mango` of this arr2
print("After removing mango: ", arr2)
print()


print("Array Concatenation")
# Concate two array
arr3 = [1, 2, 3]
arr4 = [4, 5, 6]
arr5 = arr3 + arr4
print("arr3 + arr4: ", arr5)
print()


print("Array Repeatation")
# Repeat the array with x number of times
arr6 = ['a']
arr6 = arr6 * 5
print(arr6)
print()


print("Array slicing")
arr = [1, 2, 3, 4, 5, 6]
print("Initial array: ", arr)
arr1 = arr[1:4]
print("Sliced array [1:4]: ", arr1)
arr2 = arr[:3]
print("Sliced array [:3]: ", arr2)
arr2 = arr[-3:-1]
print("Sliced array [-3:-1]: ", arr2)
print()


print("Multidimensional Array")
arr = [
    [1, 2, 3],
    [4, 5, 6],
]
print(arr[0][0])