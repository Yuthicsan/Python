#The rock is assigned to the player_choice using assignment oparator

from ast import Global


player_choice = "rock"
computer_choice = "paper"

# Calculating using the assinged variables

Today_price = 50
Quantity = 5

Total_cost = Today_price * Quantity
print(Total_cost) 


Today_price = 50
Quantity = 5
Today_price = 65 # we can change the value of the same variable

Total_cost = Today_price * Quantity
print(Total_cost) 



#we can assingn a variable top the other variable

a = 10  # a = 10
b = a   # a = 10 , b = 10
a = 20  # a = 20 , b = 10
 
print(a) # 20


#Types of variables

Value = 10      #int
value = -23     #int   
Value = 10.056  #float  
Value = "Types" #string
Value = True    #boolean
Value = None    #NoneType

print (type(Value))



#assigning multiple values to multiple variables

x, y, z = 5, 10, 15
print(x, y, z)



#assigning the same value to multiple variables



a = b = c = 10
print(a, b, c)


#Swapping the values of two variables


A = 10
B = 20
C = A
A = B
B = C
print(A, B)

a = 10
b = 20
a, b = b, a
print(a, b)



# Naming rules for variables

#1. Starting with a letter or an underscore

Fruit = "Apple" #valid
_fruit = "Mango" #valid
#2fruit = "Banana" #invalid

#2.No spaces

todays_price = 50 #valid
#Todays price = 50 #invalid

#3. can contain numbers but not start with them

fruit1 = "Orange" #valid
#1fruit = "Grape" #invalid

#4. can't use reserved keywords

#if = "value" #invalid

#5. Case sensitive

Fruit = "Apple" #valid
fruit = "Mango" #valid # they both are different variables



#arrguments assinment

price = 50 

price +=5  #price = price + 5

price *=2  #price = price * 2

price /= 5  #price = price / 5

price -=10  #price = price - 10

price //=10 #price = price // 10

price %= 10 #price = price % 10

price **= 10  #price = price ** 10
print(price)



#Local and Global variables

price  = 40
Quantity = 5

def calculate_price():
    price = 50 #local variable
    global Quantity #global variable    
    Quantity = 10 #global variable
    print(price)

calculate_price()
print(price)
print(Quantity)


#deleting a variable
del price
del Quantity