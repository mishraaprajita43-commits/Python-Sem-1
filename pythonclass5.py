# tuple (immutable)
tup1=(1,2,3,4)
print(type(tup1))
tup=(2)
print(type(tup))

tup2=(1,"string",3.4)
print(tup2)

tup0=(0,1,2,3)
tup1=(4,5,6)
tup2=tup0+tup1  # nesting in tuple
print(tup2)

#for while loop is also use there

#dictionaries
#(key(unique):value(can be dulicate))
d1={
    1:"ritika",2:"siddhi",3:"ujjwal"
}
print(d1)
print(d1.get(1)) # 1 is the value of key not index
d1[4]="vishal" #for add more values
print(d1)
for key in d1:
    print(key)

for value in d1.values():
    print(value)

for keys,value in d1.items():
    print(f"{key}:{value}")

d2={"mayank":98,"ajay":87,"rahul":56,"ram":40}
print(d2)

for name,score in d2.items():
    if score>50:
        print(name,"Pass")
    else:
        print(name,"fail")

d1={
    1:"riya",2:"radha",3:"ritu"
}
for keys,values in d1.items():
    print(f"{keys}:{values}")

for keys in d1.keys():
    print(keys)
for values in d1.values():
    print(values)

d1[4]="isha"
print(d1)

d2={"mayank":98,"ram":87,"riya":67,"ritu":77,"raj":80}
for name,score in d2.items():
    if score>=80:
     print(name,"pass")
    else:
        print(name,"fail")