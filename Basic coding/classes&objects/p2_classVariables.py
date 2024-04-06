# CLASS VARIABLES 

#1.
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

emp1 = Employee('Corey','Taylor',50000)

emp1.inc=1.05
print(Employee.inc)
print(emp1.inc)
print(emp1.pay)
emp1.apply_inc()
print(emp1.pay)

Employee.inc = 1.6
print(Employee.inc)
print(emp1.inc)

print(emp1.__dict__)

#2.

class Employee:
    n=0 #everytime an instance is created n is assigned to 0
    inc=1.04
    def __init__(self,first,last,pay): # init runs on object creation 
        Employee.n+=1 #everytime an instance is created Employee.n gets incremented
        self.n+=1 #everytime an instance is created the instance's n get incremented i.e. n+1
        self.x=self.n
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@company.com'
    
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    def apply_inc(self):
        self.pay=int(self.pay * self.inc)

#Employee.n=0 can be initialised outside as well
print(Employee.n)

emp1 = Employee('Corey','Taylor',50000)
print(Employee.n,emp1.n,emp1.x)
emp2 = Employee('Corey','Herd',10000)
print(Employee.n,emp2.n,emp2.x)


