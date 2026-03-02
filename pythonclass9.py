# class Dog:
#     species="canine"
#     def _init_(self,name,age):
#         self.name=name
#         self.age=age
# dog1=Dog("budding",3)
# print(dog1.name)
# print(dog1.species)

# dog2=Dog("remo",6)
# print(dog2.name)
# print(dog2.age)

# class Dog:
#     species="canine"

# obj1=Dog()
# obj1.name="a"
# obj1.age="b"

# print("name:",obj1.name)
# print("age:",obj1.age)
# print("species:",obj1.species)

# class car:
#     def _init_(self,brand,color):
#         self_brand=brand
#         self_color=color
#         car1=car("abc","xyz")

# class student:
#     course="btech"
# obj1=student()
# obj1.name="a"
# obj1.rollno="4"

# print("name",obj1.name)
# print("rollno",obj1.rollno)

# class Student:
    
#     def __init__(self,fullname,marks):
#         self.name=fullname #obj attr>class attr
#         self.marks=marks
#         print("adding new student in data")
    
# s1=Student("karan",88)
# print(s1.name,s1.marks)

# class Student:
#     college_name="ABC college"
#     # name="anonymous" #class attr
    
#     def __init__(self,fullname,marks):
#         self.name=fullname #obj attr>class attr
#         self.marks=marks

#     def welcome(self):
#         print("welcome student",self.name)

#     def get_marks(self):
#         return self.marks
    
# s1=Student("karan",88)
# s1.welcome
# print(s1.get_marks())

# class dog:
#     def __init__(self,name):
#         self.name=name
#     def display_name(self):
#         print(f"dog name:{self.name}")

# class labrador(dog):
#     def sound(self):
#         print("labrador woofs ")

# class guidedog(labrador):
#     def guide(self):
#         print(f"{self.name }guides the way!")

# class friendly:
#     def greet(self):
#         print("friendly")
# class goldenretriever(dog,friendly):
#     def sound(self):
#         print("goldenretriever barks")
# lab=labrador("remo")
# lab.display_name()
# lab.sound()

#important questions
#write a python program using multilevel inhertance where class vehicle  stores brand and model.
#class car inherit vehicle and adds scating capacity.
#class electric car inherit car and adds battery range 
#display all details of electric car 
#************************
# class vehicle:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
# class car(vehicle):
#     def _init(self,brand,model,seating_capacity):
#      super().__init__(brand,model)
#      self.seating_capacity=seating_capacity
# class electriccar(car):
#     def _init_(self,b,m,seating_capacity,battery-range):
#      super()._init_(b,m,seating_capacity,battery-range)
#      self.battery-range=battery-range
#     def display(self):
#         print("display")

# class calculator:
#    def add(self,a=None,b=None):
#       if a is not None and b is not None:
#          print("Sum",a+b)
#       elif a is not None:
#          print("Single value=",a)
#       else:
#          print("No Values Provided")
# c=calculator
# # c.add()
# c.add(10)
# c.add(10,20)

# #polymorphism
# class Animal:
#    def Sound(Self):
#       print("animal make diff sounds")
# class Dog(Animal):
#    def sound(self):
#       print("dog barks")

# d=Dog()
# d.sound()
# #operator persisdence
# #b o d m a s