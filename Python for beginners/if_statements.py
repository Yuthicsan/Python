# if statement executes a block of code only when its condition is true

mark = int(input("enter a number:"))

if mark >= 90:
    print("Grade A")
elif mark >= 75:
    print("Grade B")
elif mark >= 60:
    print("Grade C")
elif mark >= 40:
    print("Grade D")
else:
    print("Fail")

# nested if statement
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Underage")

# False , None , 0 and 0.0 , "" (empty string) ,[ ] (empty list) , {} (empty dictionary)
name = ""

if name:
    print("Name provided")
else:
    print("Name is empty") # this will be executed



    