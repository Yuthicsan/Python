from collections import Counter , namedtuple , OrderedDict ,defaultdict ,deque

# collections is a datatype provides alternative to python containers

# Counter

a = "aaaaabbbbcccdde"
my_counter = Counter(a)
print(my_counter)

print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())

my_list = [0, 1, 0, 1, 2, 1, 1, 3, 2, 3, 2, 4]
my_counter = Counter(my_list)
print(my_counter)

# most common items
print(my_counter.most_common(1))

print(list(my_counter.elements()))
print(list(set(my_counter.elements())))


# namedTuple

# create a namedtuple with its class name as string and its fields as string
Point = namedtuple('Point','x, y')
pt = Point(1, -4)
print(pt)
print(pt._fields)
print(type(pt))
print(pt.x, pt.y)

Person = namedtuple('Person','name, age')
friend = Person(name='Tom', age=25)
print(friend.name, friend.age)


# OrderedDict

ordinary_dict = {}
ordinary_dict['a'] = 1
ordinary_dict['b'] = 2
ordinary_dict['c'] = 3
ordinary_dict['d'] = 4
ordinary_dict['e'] = 5
print(ordinary_dict)

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['e'] = 5
print(ordered_dict)

# Iterating always ordered

for k, v in ordinary_dict.items():
    print(k, v)


# DefaultDict


d = defaultdict(int) # 0
d['yellow'] = 1
d['blue'] = 2
print(d.items())
print(d['green'])

d = defaultdict(list) # []
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 5)]
for k, v in s:
    d[k].append(v)

print(d.items())
print(d['green'])


#deque

d = deque()

d.append('a')
d.append('b')
print(d)

d.appendleft('c')
print(d)

print(d.pop())
print(d)

print(d.popleft())
print(d)

d.clear()
print(d)

d = deque(['a', 'b', 'c', 'd'])

# extend at right or left side
d.extend(['e', 'f', 'g'])
d.extendleft(['h', 'i', 'j']) 
print(d)

print(d.count('h'))

# rotate 1 positions to the right
d.rotate(1)
print(d)

# rotate 2 positions to the left
d.rotate(-2)
print(d)


