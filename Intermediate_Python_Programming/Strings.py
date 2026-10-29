#Strings immutable , sequence 

my_string = "Hello"
my_string = "I' m  a 'Geek'"

# escaping backslash
my_string = 'I\' m  a "Geek"'
my_string = 'I\' m a \'Geek\''
print(my_string)

my_string = """Hello
                World"""
print(my_string)

# backslash if you want to continue in the next line
my_string = "Hello \
                World"
print(my_string)

#accessing 

print(my_string[0])
print(my_string[-1])

#slicing or substring

b = my_string[1:3] 
print(b)
b = my_string[:5] 
print(b)
b = my_string[6:] 
print(b)
b = my_string[::2] 
print(b)
b = my_string[::-1] 
print(b)


#concatenation

print("Hello" + " " + "Tom")

#iterating

my_string = 'Hello'
for i in my_string:
    print(i)


#check if the char is there

if "e" in "Hello":
    print("yes")
if "llo" in "Hello":
    print("yes")


# methods

my_string = "     Hello World "

# remove white space
my_string = my_string.strip()
print(my_string)

# number of characters
print(len(my_string))

# Upper and lower cases
print(my_string.upper())
print(my_string.lower())

# startswith and endswith
print("hello".startswith("he"))
print("hello".endswith("llo"))

# find first index of a given substring, -1 otherwise
print("Hello".find("o"))

# count number of characters/substrings
print("Hello".count("e"))

# replace a substring with another string (only if the substring is found)
message = "Hello World"
new_message = message.replace("World", "Universe")
print(new_message)

# split the string into a list
my_string = "how are you doing"
a = my_string.split()
print(a)
my_string = "one,two,three"
a = my_string.split(",")
print(a)

# join elements of a list into a string
my_list = ['How', 'are', 'you', 'doing']
a = ' '.join(my_list)
print(a)


# Format

# use braces as placeholders
a = "Hello {0} and {1}".format("Bob", "Tom")
print(a)

# the positions are optional for the default order
a = "Hello {} and {}".format("Bob", "Tom")
print(a)

a = "The integer value is {}".format(2)
print(a)

# some special format rules for numbers
a = "The float value is {0:.3f}".format(2.1234)
print(a)
a = "The float value is {0:e}".format(2.1234)
print(a)
a = "The binary value is {0:b}".format(2)
print(a)

print("Hello %s and %s" % ("Bob", "Tom"))
val =  3.14159265359
print("The decimal value is %d" % val)
print("The float value is %f" % val)
print("The float value is %.2f" % val)


# f-Strings

name = "Eric"
age = 25
a = f"Hello, {name}. You are {age}."
print(a)
pi = 3.14159
a = f"Pi is {pi:.3f}"
print(a)
a = f"The value is {2*60}"
print(a)