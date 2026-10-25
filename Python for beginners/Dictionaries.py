def get_choices():
    player_choice = "rock"
    computer_choice = "paper"
#A dictionary is a collection of key : value pairs
    choices = {"player": player_choice ,
                "computer" : computer_choice}#KEYS SHOULD BE UNIQE 
    return choices

choices = get_choices()
print(choices)


# Creating a dictionary and printing the values
student = {
    "name": "YUTHICSAN",
    "age": 20,
    "department": "CSE",
    "cgpa": 8.2
}

print(type(student))

print(student["name"])
print(student["age"])
print(student.get("department")) #using get method to access the value of a key
print(student.get("department", 0)) #if the key is not present it will return 0


student["year"] = 3 #adding the value
student["age"] = 21 #updating the value

student.pop("year")#removing the key value pair
student.popitem()#removing the last key value pair

print(student)

copied = student.copy() #copying the dictionary
print(copied)

combined = choices | student #used for comining two dictionaries
print(combined)