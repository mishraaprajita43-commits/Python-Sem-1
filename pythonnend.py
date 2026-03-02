# for i in range (1,6):
#     for j in range(i):
#         print(i,end=" ")
#     print()

# for i in range (1,6) :
#     for j in range(1,i+1):
#         print("*",end=" ") 
#     print()

# set
# set1={1,2,3,4,5}
# print(set1)

# set2={1,2,2,3,3,4}
# print(set2)

# set3={}
# print(set3)




# balance=500
# while True:
#     print("1.check,2.deposit,3.function,4.withdrow")
#     ch=int(input("choice:"))
    
#     if ch==1:
#         print("Balance=",balance)

#     elif ch==2:
#         balance+=float (input("amount"))


#     elif ch==3:
#         amt=float(input("amount:"))
#         if amt <= balance:
#             balance-+amt
#         else:
#             print("Insufficient balance")
#     elif ch==4:
#         break



# import pandas as pd

# df = pd.DataFrame({
#     "EmpID":[1,2,3],
#     "Name":["Aman","Riya","Neha"],
#     "Dept":["HR","IT","HR"],
#     "Salary":[30000,40000,35000]
# })

# print(df[df["Dept"] == "HR"])
# df["Salary"] = df["Salary"] * 1.10
# print("Average Salary:", df["Salary"].mean())



# 1 to 50 , divisible by 3 and 5 , not both 
# for i in range(1, 51):
#     if i % 3 == 0 and i % 5 != 0:
#         print(i)
#     elif i % 5 == 0 and i % 3 != 0:
#         print(i)

# #qs.23 .1.Encapsulation
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.__marks = marks   # private variable

# # 2. Inheritance
# class Animal:
#     def speak(self):
#         print("Animal speaks")

# class Dog(Animal):
#     pass

# # 3. Polymorphism
# class Bird:
#     def sound(self):
#         print("Bird sound")

# class Sparrow(Bird):
#     def sound(self):
#         print("Chirp")

# # 4. Abstraction
# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# # qs.24.Inheritance Example
# class Engine:
#     def start(self):
#         print("Engine started")

# class Car(Engine):
#     pass

# # Composition Example
# class Engine:
#     def start(self):
#         print("Engine started")

# class Car:
#     def __init__(self):
#         self.engine = Engine()

#     def drive(self):
#         self.engine.start()

# # 25. Python Program to Read a CSV File Using csv Module
# import csv

# with open("data.csv", "r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)


# def add (*arrg):
#     print(arrg)
# add(10,20,30)

# def info (**kaarg):
#     print(kaarg)
# info(name="aprajita",age=18,course="python ")


# import numpy as np
# matrix=np.array ([
#                  [1,2,3,4],
#                  [4,5,6,7],
#                  [9,2,3,4],
#                  [2,4,5,9,]
#                  ])
# print (matrix)


# for i in range (1,6):
#     if i == 3:
#         break 
#     print(i)

y=(3+4)*2**(1+1)//3-1
print(y)