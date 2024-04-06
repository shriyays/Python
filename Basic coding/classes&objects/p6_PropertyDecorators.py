# PROPERTY DECORATORS

# - gives our class attributes
# - works like getter, setter, and deleter functionalities.
# - decorators let us use a method as a variable.


class Employee:
    
    def __init__(self,first,last):
        self.first=first
        self.last=last
        #self.email=first+'.'+last+'@company.com'
        #returns the og email itself , doesn't get updated 
    
    @property
    def email(self):
        return self.first+'.'+self.last+'@company.com'
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
emp=Employee("John","Smith")
emp.first="Jim"
print(emp.first)

# without property decorators
''' 
print(emp.email())
print(emp.fullname())
'''

#with property decorators 
print(emp.email)
print(emp.fullname)