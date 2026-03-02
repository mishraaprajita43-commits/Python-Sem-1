#arbitrary arguments(randon values)
def add_all(*nums):
    print(sum(nums))
add_all()
add_all(3)
add_all(4,5)

def multi(*nums):
    result=1
    for n in nums:
        result*=n
    print(result)
multi(3,5,6)

#arbitrary keyword arguments(**keyargs)
def person(**info):
    print(info)
person(name='xyz',age=12)

#recurrsive fn(when fn call itself)
# if base condition:
#        return some_value
#     else:def function_name(parameters):
    
#         return function_name(modified_parameters)

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))

#sum of first N natural no.s
def sum_n(n):
    if n==1:
        return 1
    else:
        return n+sum_n(n-1)
print(sum_n(4))

def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(5))

#what are columns and its type
#list comparihsion
#what are data str sata type immutable and mutable with examples
#explain default argument, position argument ,keyword argument with exam how do differ in output
#difference bw arbitrary argument and keyword arbitrary
#difference bw == and =
#what are python keywords
#difference between list and set with exzmples
#what are the rules for naming in python
# difference bw / and //
#
# write a python program
# show operator precedence in action
# x=16+4*3**2//10-1
#print the result and show how pythin evaluate it
# compare different method of formated output and compare
# calculator for basic calculation(+-*/) condition statment, loops, f string
#     difference bw continue and break
# list set tuple mutable with example how to add and excess element
# write python fn to compute factorial recurrence ......