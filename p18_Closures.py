# CLOSURES 

# A closure is an inner function that remembers and has access to variables in the local
# scope in which it was created even after the outer function has finished executing.

# Closure closes over free variables from their environment


def outer():
    message="Message"

    def inner():
        print(message)#free variable
    
    #return inner() #calls function and returns its results
    return inner #return function

#outer()
func=outer()
print(func)
print(func.__name__)
func()


#with arguments
def outer(msg):
    message=msg

    def inner():
        print(message)
    
    return inner

hi_func=outer("Hi")
hello_func=outer("Hello")

hi_func()
hello_func()