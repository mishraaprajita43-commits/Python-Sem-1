# exception handling
#  try:
#    a=int(input("enter first no."))
#    b=int(input("enter second no."))
#    result=a/b
#    print("result:",result)
# except:
#   print("cannot divide by zero")

#   write a program if enter the str display invalid number
# try:
#     a=int(input("enter first no."))
#     print(a)
#    print("invalid number")
# try:
#    a=int(input("enter first no."))
#    b=int(input("enter second no."))
#    result=a/b
#    print("result:",result)
# except ZeroDivisionError :
#   print("cannot divide by zero")

#   given a list a=[20,30,None] convert  the first 2 element to int and add them. handle value and type erroe in except bob

# a=['20','30',"hello"]
# try:
#    total = int(a[0])+int(a[1])
#    print(total)
# except (ValueError,TypeError) as e:
#    print("Error Occurred",e)

# file handling
# format
# open("filename.txt,mode")

# f=open("data.txt","r")
# f.close()

# f=open("data.txt","w")
# f.write("  ")
# f.close()

# with open("ex.txt",'w') as f:
#    f.write("hello class , I am sick")

# with open("ex.txt",'a') as f:
#    f.write("this is append txt")

# with open ("ex.txt",'r') as f :
#    data=f.read()
#    print(data)

# try:
#    f=open("data.txt","r")
#    print(f.read())
# except:
#    print("file is not found")

# **************************************
# Q1 develop a python class book with attributes title ,anthor,isbn & status & methods to
# --diaplay book details
# --issue/return a book(status)
# --save details to a-txt file library.txt
# use try-except for file & input handling
# write a main program the allows user to add & view books using a menu driven loop
# ***************************************

# Q2 design a class bank account with artibute acc no name balance and include method deposite withdraw 
# display try accept incase insufficient balance demostrate transition for atlist  3 account using objects 

class BankAccount:
    def __init__(self, accountno, name, balance=0):
        self.accountno = accountno
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited:", amount)
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance")

    def display(self):
        print(self.accountno, self.name, self.balance)


acc1 = BankAccount(101, "Mayank", 5000)
acc2 = BankAccount(102, "Jiya", 2000)
acc3 = BankAccount(103, "Aman", 1000)

acc1.display()
acc2.display()
acc1.withdraw(100)
acc2.deposit(500)
acc1.display()
acc2.display()

# develop a pyhton class book with attribute title auother isbl
#  and status method display book details issue or return a book update status save details to a text file library.txt use try except 
# for file input handling    write a main program to user add book using a deriven loop   












      