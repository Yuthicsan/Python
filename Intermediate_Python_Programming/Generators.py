# Generators are functions that can be paused and resumed on the fly, returning an object that can be iterated over


def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1

cd = countdown(3)

print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd)) # this will raise a StopIteration


cd = countdown(3)
for x in cd:
    print(x)


cd = countdown(3)
sum_cd = sum(cd)
print(sum_cd)
cd = countdown(3)
sorted_cd = sorted(cd)
print(sorted_cd)


#Generator saves memory
# without a generator, the complete sequence has to be stored here in a list
# with a generator, no additional sequence is needed to store the numbers


def firstn(n):
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
    return nums

sum_of_first_n = sum(firstn(1000000))
print(sum_of_first_n)
import sys
print(sys.getsizeof(firstn(1000000)), "bytes")


# Fibonacci numbers using generators

def fibonacci(limit):
    a, b = 0, 1 # first two fibonacci numbers
    while a < limit:
        yield a
        a, b = b, a + b

fib = fibonacci(30)
print(list(fib))


# generator expression
mygenerator = (i for i in range(1000) if i % 2 == 0)
print(sys.getsizeof(mygenerator))

# list comprehension
mylist = [i for i in range(1000) if i % 2 == 0]
print(sys.getsizeof(mylist))


#Concept behind a generator


class firstn:
    def __init__(self, n):
        self.n = n
        self.num = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num < self.n:
            cur = self.num
            self.num += 1
            return cur
        else:
            raise StopIteration()
             
firstn_object = firstn(1000000)
print(sum(firstn_object))