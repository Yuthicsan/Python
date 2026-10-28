#Class: A definition or blueprint.
#Object: A particular instance created from a class.


#self refers to the object whose method is running
class Student:
    def __init__(self, name, age):#initializing objects
        self.name = name
        self.age = age

student1 = Student("Arun", 19)
student2 = Student("Priya", 20)#object creation

print(student1.name)
print(student2.name)
print(student1.age)
print(student2.age)

