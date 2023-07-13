# IMPORTING MODULES

'''__pycache__ is a directory that is created by the Python interpreter when it imports a
 module. It contains the compiled bytecode of the module, which can be used to speed up 
 subsequent imports of the same module.'''


import my_module
courses = ["History","Math","English","Art"]
sub="Art"
index = my_module.find_index(courses,"Art")
print(sub,"found at", index)


import my_module as mm
#index = my_module.find_index(courses,"Art") - NameError: name 'my_module' is not defined
index = mm.find_index(courses,sub)
print(sub,"found at", index)

from my_module import find_index, test
index = find_index(courses,"Math")
print("Math: ",index)
print("test:",test)


from my_module import find_index as fi
index = fi(courses,"pe")
print(index)


from my_module import *    #import everything from the said module


