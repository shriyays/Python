# CLASSES AND INSTANCES

# Attributes - data & methods - functions

#1. creating a class and two instances
class Employee :
    pass

emp1 = Employee()
emp2 = Employee()



#2. init method : 
''' The __init__ function is called every time an object is created from a class.
    The __init__ method lets the class initialize the object's attributes and serves no other purpose. 
    It is only used within classes.'''
class Employee:
    # the first argument in a method inside a class definition is for to assign the instance to it 
    # in order to access and operate on its attributes
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@company.com'

emp1 = Employee('Corey','Taylor',50000) # instantiation 
#self=Emplyoee(first,last,pay)
''' Therefore, when emp1 is created (an instance of class Employee) emp1 is assigned to self, 
    first = 'Corey', last ='Taylore' and pay = 50000, 
    and emp1's first = first = "Corey" and so on.
    So, if self.first is not assigned to first we cannot access first outside the class using emp1 
    i.e. emp1.first, emp1.last or emp1.pay will not exist unless assigned to.
'''
emp2 = Employee('Test','User',10000)

print(emp1.email,emp2.email,sep="\n")
salary = emp1.pay
print(salary)




#3. other methods 
class Employee:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@company.com'


    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
emp1 = Employee('Corey','Taylor',50000)
print(emp1.fullname())
print(Employee.fullname(emp1))