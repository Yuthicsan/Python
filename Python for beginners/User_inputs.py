# user input
#it takes the input form user and stores it in a variable
variable = input("Message shown to the user: ")

print(variable)
print(type(variable)) #by default the input is stored as string

a = int(input("Enter a number: ")) #converting the input to integer
b = int(input("Enter another number: "))
c = a + b
print(c)


#types of conversion

a = int(input("integer"))
b = float(input("float"))
c = bool(input("boolian"))
d = str(c)


#Invalid user input


try:
    age = int(input("Enter your age: "))

    if age < 0:
        print("Age cannot be negative.")
    else:
        print("Your age is:", age)

except ValueError:
    print("Invalid input. Please enter a whole number.")
