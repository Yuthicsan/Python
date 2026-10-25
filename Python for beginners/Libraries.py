#library is a collection of prewritten code 

#there many import library 
import random as r # using alias
from math import sqrt, pow, ceil, floor, pi #importing a specific function
import datetime
import collections
import numpy as np # type: ignore

number = 25

print("square root:", sqrt(number))
print("square:", pow(number, 2))
print("ceil:", ceil(4.2))
print("floor:", floor(4.8))
print("val of pi:", pi)


numbers = np.array([10, 20, 30, 40])

print("Array:", numbers)
print("Sum:", np.sum(numbers))
print("Average:", np.mean(numbers))


