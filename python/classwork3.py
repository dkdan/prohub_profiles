# 1. write a simple program to loop through a list of fruit
# fruits=['watermelon','apple','banana','oranges','cherry','pineapples']
# for i in fruits:
#     print(f'{i}')

# # write a simple program to print your name 6 times
# for i in range(0,6):
#     print('Daniel')


# write a program to print a factorial of any number
arg1=int(input('type a number: '))
x=0
p=1
for i in range(0,arg1):
    p=p*(arg1-i)
    print(p)

print(p)