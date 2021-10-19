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

what = input("what do you want to do? ")
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