#set is mutable ,elements are unordered ,duplicates are not allowed
set1={1,2,3,3,4,5}
print(set1)

set2={1,2,3,4,4,4,5,5}
print(set2)

#create empty set
set3=set()
set={}


# set4=set("python prog","hello","class1")
# print(set4)

# set5=set([1,2,3])
# print(set5)

# file=(1,2,3,3,4)
# tuple=["name","rollno","class","class"]
# set8=set(tuple)
# print(set8)

# dict={"class":13,"rollno":2501010318,"name":"neetu"}
# set9=set(dict)
# print(set9)

set10={1,2,3}
set10.add(4)        #.add() is called as method add is for add single element
set10.update([5,6]) #for multiple elements
print(set10)

set11={"abc","def","gef","hello","bye"}
for item in set11:
    print(item,end=" ")
print("abcc" in set11)

set12={1,2,3,4,4}
set12.remove(3)
set12.discard(10)  #if the element is not in set so in output error is not show
print(set12)

# f=frozenset([set12]) #add,remove,dicard is not possible
# print(f)           #output frozenset({1,2,4})

# fset=frozenset([  ]) #create empty set

# set1=set()
# for i in range(1,6):
#  set1.add(i)
    
print(set1)

set2={"riya","sakshi","renu","komal"}
print(len(set2))

set3={"riya"}
print(len(set3))

# s="pythonprogramming"
# set_char=set(s)
# print(set_char)
# print("unique chars:",len(set_char))

set1={10,20,30,40}
set1.remove(20)
# set1.remove(50)
set1.discard(40)
set1.discard(50)
print(set1)

# s=("a","b","c","d")
# set1=set(s)
# for item in set1:
#     print(item,end="")
#     print("a" in set1)

a={1,2,3,4,5}
b={4,5,6,7,8,}
print(a|b) #for union(|)
print(a&b) #for intersection
print(a-b) #for difference output {1,2,3}
print(b-a) #output {8,6,7}
print(a^b) #for symmetric difference output {1,2,3,6,7,8}