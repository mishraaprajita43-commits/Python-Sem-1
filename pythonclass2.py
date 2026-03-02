#strings are immutable.
#s="hello python"
#   01234567891011 positive indexing 
#s="hellopython"
#            -2-1
#s[start:end] s[::] print complete sentense
#s[start:end:step]
#s[::-1] reverse print

s="INFORMATIONTECH"
print(s[0:5]) 
print(s[-4:])
print(s[2:7])
print(s[0:14:2]) #every second ch starting from index 0
print(s[11:])

s1="COMPUTERSCIENCE"
print(s1[0:8])
print(s1[8:])
print(s1[-5:])
print(s1[0:14:2]) #every alt char
print(s1[::-1])
print(len(s1)) #length of string
print(s1.upper())
print(s1.lower())

s=" COMPUTERSCIENCE " 
print(s.strip()) #for reduce space

# marks=int(input("enter your marks"))
# print("pass" if marks>=40 else "false")

# marks=int(input("enter your marks"))
# if marks>=40:
#     print("pass")
# else:
#     print("fail") # *** operators are important ***


 #list[mutable,duplicate] tuple(immutable,no duplicates) dictnory{immutable} are data structure***********
# sq=[x**2 for x in range (1,11)]
# print(sq)

# cube=[x**3 for x in range (1,8)]
# print(cube)

# even=[i for i in range (1,21) if i%2==0] #comparising operators ka output true ta false hota h esliye if condition use karna hota h 
# print(even)

# num=[1,2,3,4,5] #list comprehansion
# num1=[i*5 for i in num]
# print(num1)

# num=[10,25,30,45,50,65]
# num1=[i for i in num if i>30]
# print(num1)

# def cube(n):return n**3
# num=[1,2,3,4,5]
# cube1=[cube(x) for x in num]
# print(cube1)

# num=[1,2,3,4,5]
# nat=["even" if n%2==0 else "odd" for n in num]
# print(nat)

# pairs=[(x,y) for x in [1,2] for y in [3,4]]
# print(pairs)

# num=range(20)
# filter=[n for n in num if n%2==0 if n>10]
# print(filter)

# num=[1,2,3]
# unique=[(n,n**2,n**3) for n in num]
# print(unique)

# words=["hello",'python']
# length=[len(w) for w in words]
# print(length)

# num=[1,2,3,3,4,5,5,6]
# lists=list({i for i in num})
# print(lists)

# name=['mayank','ajay']
# score=[96,90]
# dic=[f"{n}:{s}" for n,s in zip(name,score)]
# print(dic)