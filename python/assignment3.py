# 1. Adding two numbers but one should have a default parameter 
def addin(arg1,arg2='5'):
    newval = int(arg1) + int(arg2)
    return newval

arg1= int(input('select first number: '))
arg2 = input('Select second numer - default is 5: ')
agres= addin(arg1,arg2)
print(agres)

# # 2. A simple calculator to add three numbers, and add two of the numbers and subtract one number 
# def addinsub(arg1,arg2,arg3):
#     newval= arg1 + arg2 
#     newval = newval-arg3
#     return newval

# arg1= int(input('Select first number: '))
# arg2 = int(input('Select second numer: '))
# arg3 = int(input('Select Third numer: '))
# agres= addinsub(arg1,arg2,arg3)
# print(agres)

# 3.Write a program to compare three number entered by the user and display the greatest among the three
# def comparef(arg1,arg2,arg3):
#     if (arg1 <= arg3 >= arg2):
#         return arg3
#     elif (arg3 <= arg1 >= arg2):
#         return arg1
#     elif (arg3 <= arg2 >= arg1):
#         return arg2
    

# print('compare 3 numbers showing the largest of them---->')
# arg1= int(input('Select first number: '))
# arg2 = int(input('Select second numer: '))
# arg3 = int(input('Select Third numer: '))
# agres= comparef(arg1,arg2,arg3)
# print(agres)
def add(arg1,arg2):
    ans= arg1 + arg2
    return ans
def subtract(arg1,arg2):
    ans=arg1 - arg2
    return ans
def divide(arg1,arg2):
    ans=arg1 / arg2
    return ans
def times(arg1,arg2):
    ans= int(arg1) * int(arg2)
    return ans

what = input("what do you want to do? add, subtract, divide or times")
if what=='add':
    arg1=int(input('first number: '))
    arg2=int(input('second number: '))
    exsoln= add(arg1,arg2)
    print(exsoln)
elif what=='subtract':
        arg1=input('first number: ')
        arg2=input('second number: ')
        exsoln= subtract(arg1,arg2)
        print(exsoln)    
elif what=='divide':
        arg1=input('first number: ')
        arg2=input('second number: ')
        exsoln= divide(arg1,arg2)
        print(exsoln)
else:
        arg1=input('first number: ')
        arg2=input('second number: ')
        exsoln= times(arg1,arg2)
        print(exsoln)    

# ex2 = subtract(6,1)
# ex3 = divide(36,6)

# print(ex1)
# print(s)
# print()
# print()