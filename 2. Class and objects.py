# First class is an empty class.
# `pass` is used similar to `continue` in C++
class FirstClass:
    def __init__(self):
        pass


class ComplexNumber:
    def __init__(self, real=0, img=0):  # Constructor with parameters for real and img
        print('Complex Number class constructor invoked')
        # Dynamically creating instance variables real and img
        self.real = real  # Assign the real part to an instance attribute
        self.img = img    # Assign the imaginary part to an instance attribute
    
    def displayNumber(self):
        # Display the complex number using the instance attributes real and img
        print("{0} +  {1}j".format(self.real, self.img))



# ComplexNumber object creation
complexNumber = ComplexNumber(40, 50)
complexNumber.displayNumber()

# Complex object with new attributes
complexNumber2 = ComplexNumber(5, 6)
complexNumber2.displayNumber()
complexNumber2.newAttribute = 7
print("The new attribute ", complexNumber2.newAttribute)

# The above newAttribute can only be used in `complexNumber2`**
# print("The new attribute ", complexNumber.newAttribute)


# Printing the object
print(complexNumber2) # show the memory address

# Deleting an attribute
print("Before deletion: ", complexNumber2.newAttribute)
del complexNumber2.newAttribute
# print("After deletion: ", complexNumber2.newAttribute) # error no attribute

# delete the entire object
del complexNumber2 
print("After Deletion")
# print(complexNumber2) # error: object not found
