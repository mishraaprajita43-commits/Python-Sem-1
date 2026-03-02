# while loop
name=input("enter your name")
while name=="": # space nahi dena between strings
    print("invalid input")
    name=input("enter your name") #infinite loop se bachne ke liye bhar print karvaya h 
print("your name is",name)

age=int(input("enter your age:"))
while age<=0:
    print("age is not valid")
    age=int(input("enter your age"))
print("your age is",age)

num=int(input("enter any number:"))
fact=1
while(num>0):
    fact=fact*num
    num=num-1
print("factorial is",fact)

#slicing
#lists tuple difference
#if else false or true
#star,num pattern
#avg if else vala program
#operators type of operations with example (5)
#collector data from user find area parameter

# a.append( ) add one element
# a.extend() add extended string school='s','c','h','o','o','l'
# a.insert() position de sakte h element 
# a.clear( ) output [] baki clear ho jaega
# a.pop() position deke elements delete kr sakte h 
# a.remove() starting aala ek repiting element delete ho jaega
# 
a=[1,2,3,4,5]

a.append(7)
a.insert(5,6)
print(a)

b=["python","world","lists"] 
b.append("school")
b.extend("school")
print(b)

tup1=(1,2,3)
tup2=(4,5,6)
tup3=tup1+tup2
print(tup3)