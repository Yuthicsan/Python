#A tuple is a built-in Python data type used to store multiple values in a single variable

student = ("Arun", 20, "CSE", 8.7)

print(student)

#TypeError as it is an immutable
numbers = (10, 20, 30)

numbers[0] = 100


colors = ("red", "green", "blue", "yellow")

print(colors[0])
print(colors[1])
print(colors[-1])
print(colors[-2])#indexing


numbers = (10, 20, 30, 40, 50, 60)

print(numbers[1:4])
print(numbers[:3])
print(numbers[3:])
print(numbers[::2])
print(numbers[::-1])#slicing