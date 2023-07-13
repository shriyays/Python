#To find the location of the module that is in the same directory 

''' sys. path is a built-in variable within the sys module. 
    It contains a list of directories that the interpreter will search in for the 
    required module. When a module(a module is a python file) is imported within a 
    Python file, the interpreter first searches for the specified module among its 
    built-in modules. '''

import my_module
import sys

print(sys.path)

# format of sys.path : ['dir where files are saved', 'dir listed in the python path environment variable',
#                        'standard lib dir', 'side packages dir for third party packages']




#To find the location of the module that is in a different directory 


import sys
#print(sys.path) - ModuleNotFoundError: No module named 'my_module2'

sys.path.insert(0,"/Users/shriyays/desktop/cs/LANGUAGES/python/child_dir")
print(sys.path)

from my_module2 import num
print(num)

# or  "export PYTHONPATH=’path/to/directory’ " in linux terminal 
#     "SET PYTHONPATH=”path/to/directory”" in windows cmd

# or

import fake.my_module2
print(sys.path)




