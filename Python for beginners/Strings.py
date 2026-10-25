# A string is a sequence of characters

name = "Python"
college = "SRM University"

print(name)
print(college)

#fstring and format function
name = "Arun"
age = 20

print(f"My name is {name} and I am {age} years old.")

print("Name: {}, Age: {}".format(name, age))

print(name[0])
print(name[-3]) #indexing

print(college[0:3])
print(college[2:5])# slicing

first = "Hello"
second = "World"

result = first + " " + second
print(result) #concedination

# string functions
text = "Hello Python"

print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())
print(text.swapcase())



text = "   Python   "

print(text.strip())
print(text.lstrip())
print(text.rstrip())


print("Python123".isalnum())
print("Python".isalpha())
print("12345".isdigit())
print("   ".isspace())
print("hello".islower())
print("HELLO".isupper())

# escape charecters 

print("Hello\nWorld")
print("Name:\tArun")
print("It's Python")
print("C:\\Users\\Student")