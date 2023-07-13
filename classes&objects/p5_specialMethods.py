# SPECIAL METHODS 

'''
Special Methods are known as Dunder Methods. 
Usually and for shortcut purposes, it is called dunder instead of the double underscore.

'''

#1. "__repr__(self)" : a built-in method in Python that returns a string representation
#                      of an object. The primary purpose of __repr__ is to provide a 
#                      helpful and unambiguous representation of an object for debugging
#                      purposes. __repr__ is used by developers to recreate an object by
#                      evaluating the string returned by __repr__.

#2. "__str__(self)" : for a better representation - readability 
#                     - you convert this object into a string. 


class Employee:
    inc=1.04

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@company.com'

    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    def apply_inc(self):
        self.pay=int(self.pay * self.inc)

    
    
    def __repr__(self):
        return "Employee('{}','{}','{}').".format(self.first,self.last,self.pay)
    
    def __str__(self):
 
        return '{}-{}'.format(self.first,self.last)
    
    def __add__(self,other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())
   

emp1=Employee("corey","schafer",32442)
emp2=Employee("corey","simon",23423)
print(emp1)
'''
print(repr(emp1))
print(str(emp1))
'''
print(emp1.__repr__())
print(emp1.__str__())

print(int.__add__(1,2))
print(str.__add__('a','b'))

print(emp1+emp2)


print(len('test'))
print('test'.__len__())

print(len(emp1))
print(len(emp2))



