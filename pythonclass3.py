#for loop
#example
for x in range(1,11,2): #11 is exclusive
    print(x)

for x in range (1,21):
    if x==13:
        continue #continue ka meaning h vo alternation escape hogi
    else:
        print(x)    

for x in range (1,21):
    if x==13:
        break # 12 ke baad kuch print nahi hoga
    else:
        print(x)  

#nestings of loops
#for-for,whole-while,while-for,for-while  
for y in range (3):
 for x in range(1,10):
    print(x)

for y in range (3):
 for x in range(1,10):
    print(x,end="")  #end answer ko horizontal print karva dega
    
 print()

 rows=int(input("enter rows"))
 columns=int(input("enter colums"))
 sym=input("enter symbol")
 for x in range(rows):
    for y in range(columns):
       print(sym,end="")
    print()

rows=5
for i in range(1,6):
    for j in range (1, i+1):
        print(j,end="")
    print()

rows=5
for i in range(1,6):
    for j in range (1, i+1):
        print("*",end="")
    print()