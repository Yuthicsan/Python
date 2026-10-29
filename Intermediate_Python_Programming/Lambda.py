#Lambda functions is a small one line anonymous function
#lambda arguments: expression

# a lambda function that adds 10 to the input argument
f = lambda x: x+10
val1 = f(5)
val2 = f(100)
print(val1, val2)

def myfunc(n):
    return lambda x: x * n # lambda inside another func

doubler = myfunc(2)
print(doubler(6))

tripler = myfunc(3)
print(tripler(6))


points2D = [(1, 9), (4, 1), (5, -3), (10, 2)]
sorted_by_y = sorted(points2D, key= lambda x: x[1])
print(sorted_by_y)

mylist = [- 1, -4, -2, -3, 1, 2, 3, 4]
sorted_by_abs = sorted(mylist, key= lambda x: abs(x))
print(sorted_by_abs)

#map

a  = [1, 2, 3, 4, 5, 6]
b = list(map(lambda x: x * 2 , a))
c = [x*2 for x in a] # both are equal
print(b)
print(c)

#filter

a = [1, 2, 3, 4, 5, 6, 7, 8]
b = list(filter(lambda x: (x%2 == 0) , a))
c = [x for x in a if x%2 == 0] # both are equal
print(b)
print(c)

#reduce

from functools import reduce
a = [1, 2, 3, 4]
product_a = reduce(lambda x, y: x*y, a)
print(product_a)
sum_a = reduce(lambda x, y: x+y, a)
print(sum_a)