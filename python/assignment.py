# 1. a) Create a list on fruits, print all the fruits.
list=["orange", "mango", "guava", "banana", "strawberry"]
print(list)
# b) Add a fruit at any position and also add at the end of the list 
list.append("lemons")
list.insert(-3,"pawpaw")
print(list)
# c) Access a particular student and print it out
student=["dan", "sam", "fashola", "akpors","Feyisara","Nikemi"]
print("Name of one student from the class: ")
print(student[2])
# d) remove an item at the end and any position in the list 
print("Deleted one item at the end: ")
del student[len(student)-1] 
print(student)
print("Deleted one item: ")
print(student)

# 2. Create a set and tuple
print("this is a tuple: ")
simpletuple=("orange","Looks like orange","not orange")
addtuple=('smells like orange',)
# b) add an item to both the set and tuple.
print("new tuple simple + new item")
newtuple = simpletuple + addtuple
print(newtuple)
# c) delete an item from both the set and tuple
# del newtuple[-1] tuple object does not support item deletion
print(newtuple)
# d) remove an item from a set
# e) delete the set and tuple
del newtuple
del simpletuple
print('tuples deleted')

# 3.a) create a dictionary of prohub students
prohub={'name=':'Daniel','name=':'femzy','name=':'Tega','name=':'Emma','name=':'Dayo','name=':'Osas'}
print('students in prohub: ')
print(prohub)
# b) add two other keys and value to the dictionary 
prohub.update({
    'name=':'Mr Nosa',
    'name=':'AnchorsoftOga'
})
print('Added two individuals to prohub: ')
print(prohub)
# c) create a copy of the prohub student to Anchorsoft student 
anchorsoftstudent=prohub
# d) add a key and value to the new copied student 
anchorsoftstudent.update({
    'name=':'Secretary'
})
anchorsoftstudent.update({
    'name=':'2nd Tutor'
})
print('Another dictionary of anchorsoft members: ')
print(anchorsoftstudent)
# e) create a list of 3 dictionary and access the second one by name, keys and item
newcommers=[
    {
        'name':'Daniel',
        'age':20
        'address':'Ikeja'
    },
    {
        'name':'Tega',
        'age':24,
        'address':'Ipaja'

    },
    {
        'name': 'Femi'
        'age':'23'
        'address':'Allen'
    },
]
print('you will find daniel in'.newcommers[1][name])

# dict1={
#     'state1=':'Lagos',
#     'state1=':'Kano',
#     'state3=':'Abuja'
# }
# dict2={
#     'Country1=':'Nigeria',
#     'Country2=':'Biafra',
#     'Country3=':'Ghana',
#     'country4=':'Southy'
# }
# Japa={
#     'country1=':'Germany',
#     'country2=':'Netherland',
#     'country3=':'Jand',
#     'country4=':'Yankee',
#     'country5=':'Canada'    
# }  
print('I will get a job in {} or {}'.format("Japa(country5)"))