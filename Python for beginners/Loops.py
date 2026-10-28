#They help you repeat instructions without writing the same code again and again


#for loop


fruits = ["Apple", "Mango", "Banana"] # it can be str list or any thing to iterate

for fruit in fruits:
    print(fruit)

for i in range(5):#range fn is used for stop the fn with the range
    print(i)

#while loop

i = 1

while i <= 5:
    print(i)
    i += 1


for i in range(1, 11):
    if i == 5:
        break# it is used to break in b/w the fn
       #continue Skips only the current iteration
    print(i)


#enumerate fn

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)



