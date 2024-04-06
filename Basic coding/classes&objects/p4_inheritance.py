# INHERITANCE

# Parent Class
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

#Child Class

#1.
class Developer(Employee):
    pass

dev1=Developer("John","Casey",8000)
print(dev1.__dict__)

'''Method Resolution Order :
        when dev1 is instantiated, init method is looked for in Developer class,
        which is not found there, hence it climbs up the inheritance chain and 
        looks for the init method in Employee.
'''
#print(help(Developer))



#2.
class Developer(Employee):
    inc = 1.10

dev2=Developer('John','Mayer',30000)
print(dev2.pay)
dev2.apply_inc()
print(dev2.pay)


#3.
class Developer(Employee):
    inc = 1.05
    def __init__(self,first,last,pay,p_lang):
        super().__init__(first,last,pay)
        #Employee.__init__(self,first,last,pay)
            #can also be used but super is more useful in case of multiple inheritance
        self.p_lang=p_lang



dev3=Developer('John','Boyd',30000,'Python')
print(dev3.email)
print(dev3.p_lang)


#4. 
class Manager(Employee):
    pass

mngr1=Manager(dev1.first,dev1.last,dev1.pay)
print(isinstance(mngr1,Manager))
print(isinstance(mngr1,Employee))
print(isinstance(mngr1,Developer))


#5.
print(issubclass(Developer,Employee))
print(issubclass(Manager,Employee))
print(issubclass(Developer,Manager))

