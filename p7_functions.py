#FUNCTIONS 

def func():
    return "FUNCTIONS!!!"

print(func().upper())

#passing arguments

def func(greeting,name="you"):
    return'{},{}!!!'.format(greeting,name)

print(func("hello","Charles"))

#passing arbitrary number of arguments 
# args : tuple of all positional arguments
# kwargs : dictionary of keywords and values
def info(*args, **kwargs):
    print(args)
    print(kwargs)

info("math","art",name="James",age=22)
#info("art",name="Johnny","football",age=20)
#  - SyntaxError: positional argument follows keyword argument

def student_info(*args, **kwargs):
    print(args,kwargs)

courses=['m',"a",'pe']
info = {'name':"John", 'age' : 41,}
         
student_info(courses,info) #courses and info get passed as positional arguments of a tuple and therefore the arguments for the dictionary will remain empty and an empty dictionary is returned 

student_info(*courses,**info) #the * 's help unpacking the respective values and passing them 

