
from itertools import product, permutations, combinations, \
combinations_with_replacement, accumulate, groupby ,count \
, cycle, repeat

# iter tools is a collection of tools for handling iterators


# Product() : computes the cartesion products

prod = product([1, 2], [3, 4])
print(list(prod))

prod = product([1, 2], [3], repeat=2)
print(list(prod)) 

# permutations() : gives all the possible output 

perm = permutations([1, 2, 3])
print(list(perm))

perm = permutations([1, 2, 3], 2)# the length of the permutation tuples
print(list(perm))

# combinations() :combination tuples will be produced in sorted order

# the second argument is mandatory and specifies the length of the output tuples.
comb = combinations([1, 2, 3, 4], 2)
print(list(comb))

comb = combinations_with_replacement([1, 2, 3, 4], 2)
print(list(comb))

#accumulate() : returns accumulated sums

# return accumulated sums
acc = accumulate([1,2,3,4])
print(list(acc))

# other possible functions are possible
import operator
acc = accumulate([1,2,3,4], func=operator.mul)
print(list(acc))

acc = accumulate([1,5,2,6,3,4], func=max)
print(list(acc))

# Groupby()

# use a function as key
def smaller_than_3(x):
    return x < 3

group_obj = groupby([1, 2, 3, 4], key=smaller_than_3)
for key, group in group_obj:
    print(key, list(group))
    
# or use a lamda expression
group_obj = groupby(["hi", "nice", "hello", "cool"], key=lambda x: "i" in x)
for key, group in group_obj:
    print(key, list(group))
    
persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25}, 
           {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]

for key, group in groupby(persons, key=lambda x: x['age']):
    print(key, list(group))


# Infinite iterators

# count(x): count from x: x, x+1, x+2, x+3...
for i in count(10):
    print(i)
    if  i >= 13:
        break

# cycle(iterable) : cycle infinitely through an iterable
print("")
sum = 0
for i in cycle([1, 2, 3]):
    print(i)
    sum += i
    if sum >= 12:
        break

# repeat(x): repeat x infinitely or n times
print("")
for i in repeat("A", 3):
    print(i)