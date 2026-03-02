# num=int(input("enter any number:"))
# if num%2==0:
#     print(num, "is even")
# else:
#     print(num,"is odd")

# def fun_name():
#   num=int(input("enter any number:"))
#   if num%2==0:
#     print(num, "is even")
#   else:
#     print(num,"is odd") 
#   fun_name()


def greet(name="xyz"):
  print("hello",name)
greet()
greet("neetu")

def power(num,exp):
  print(num**exp)

power(5,3)

def power(num,exp=2):
  print(num**exp)

power(5,4)

def area(len=3,bre=4):
  print("area",len*bre)
area()
area(4)
area(3,5)

def introduce(name,country="india"):
  print(f"my name is",{name},"i am from",{country})

introduce("neetu")

def discount(price,rate=40):
  print(price*rate/100)
discount(2000)
discount(1000,20)

def student(fname, lname):
  print(fname,lname)
student(fname="xyz", lname="abc")
student(fname="neetu",lname="sheoran")

def employee(name,age,department):
  print(f"employee {name} with {age} years old works in {department}")
employee(age=23,name="xyz",department="soet")

employee("xyz", 10, "cse dep")

def add(a,b):
  print(a+b) #positional argument

add(3,4)

def subject(name,marks):
  print(name,marks)
subject("maths" ,90)
subject("phy",95)
subject("chem",86)

def num(n):
  if n%2==0:
    print("even")
  else:
    print("odd")
num(2)

print(16+4*3**2//10-1)
print(9//10)