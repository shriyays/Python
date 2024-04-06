# "__name__()" : built-in variable which evaluates to the name of the current module. 
# Thus it can be used to check whether the current script is being run on its own or 
# being imported somewhere else.


# "__main__" : name of the environment where top-level code is run. “Top-level code” is
# the first user-specified Python module that starts running. It's “top-level” because 
# it imports all other modules that the program needs.

'''
    A Python programme uses the condition if __name__ == '__main__' to only run the code 
    inside the if statement when the program is run directly by the Python interpreter. 
    The code inside the if statement is not executed when the file's code is imported as
    a module.

'''

print(__name__)

import module_1

print(__name__)

import module_2

