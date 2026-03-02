# age=int(input("enter your age:"))
# if age<=12:
#     print("travel for free")
# else:
#     print("pay for ticket")

# marks=45
# if marks>=40:
#     print("pass")
# else:
#     print("fail")

age=25
if age<=12:
    print("child")
elif  age<=19 and age>12:
    print("teenager")
elif age<=35 and age>19:
    print("young")
else:
    print("adult")

# username="aprajita.mishra"
# password=969367
# if password=="969367":
#     print("true")
# else:
#     print("false")


# ternary
# on_true if condition else on_false
# "even" if mm%2==0 else "odd"

# marks=int(input("enter marks"))
# print("pass" if marks>=50 else "fail")

# marks=int(input("enter marks"))
# if marks<40:
#     print("fail")
# elif marks<60 and marks>40:
#     print("pass")
# elif marks<80 and marks>60:
#     print("good")
# else:
#     print("excellent")

# day=int(input("enter day range(1-7):"))
# if day==1:
#     print("monday")
# elif day==2:
#     print("tuesday")
# elif day==3:
#     print("wednesday")
# elif day==4:
#     print("thursday")
# elif day==5:
#     print("friday")
# elif day==6:
#     print("saturday")
# elif day==7:
#     print("sunday")
# else:
#     print("invalid day")


# order=int(input("enter price:"))
# print("free shipping" if order>=500 else "delivery charges")

# #write a program take marks of 4 subjests as input from the user then cal the avg of the marks assing a grade

marks1=int(input("enter physics marks"))
marks2=int(input("enter chemistry marks"))
marks3=int(input("enter maths marks"))
marks4=int(input("enter english marks"))
avgmarks=(marks1+marks2+marks3+marks4)/4
print(avgmarks)

avgmarks=int(input("enter avg marks"))

if avgmarks>=90:
    print("grade A")
elif avgmarks>=75 and avgmarks<90:
    print("grade B")
elif avgmarks>=60 and avgmarks<75:
    print("grade C")
elif avgmarks>=45 and avgmarks<60:
    print("grade D")
else:
    print("grade E")