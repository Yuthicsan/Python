#function is a set of instructions that perform a specific task
from ast import Lambda


def get_choices():
    player_choice = "rock"
    computer_choice = "paper"
    return computer_choice

#these are calling functions and storing the return values in variable
choices = get_choices()
print(choices)


def get_choices():
    player_choice = "rock"
    computer_choice = "paper"
    return computer_choice , player_choice   #Muiliple return values




#Parameters and Arguments

def Name(name): # here name is a parameter
    print("Hello " + name)


Name("Yuthi")
Name("John")    #here John is an Argument



def Name(name , age): #Muilti parameter
    print("Hello " + name + " your age is " + age)


Name("Yuthi" , "20")
Name("John" , "25") 

#Dinamic number of arguements

def sum(*args):
    total = 0 
    for n in args:
        total += n
    return total

print(sum(1, 2, 3, 4, 5))
print(sum(1, 2, 3))



#Lambda functin is a small anonymous function that can take any num of args but returns only one expression


Square = lambda x: x * x

print(Square(5))




#Recursive function is a fun which calls itself



def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))