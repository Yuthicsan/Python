#Shallow vs deep copying


#Shallow copy


import copy
list_a = [1, 2, 3, 4, 5]
list_b = copy.copy(list_a)

# not affects the other list
list_b[0] = -10
print(list_a)
print(list_b)


#Deep copies


import copy
list_a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
list_b = copy.deepcopy(list_a)

# not affects the other
list_a[0][0]= -10
print(list_a)
print(list_b)
