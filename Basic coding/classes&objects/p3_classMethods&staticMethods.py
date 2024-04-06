# CLASS METHODS AND STATIC METHODS

# Regular methods - inside a class assign the instance to the first argument.
# Class methods - assign the class to the first argument - used as constructors
#               - "@classmethod" decorator is used.
# Static methods -  don't pass anything automatically 
#                -  behave like normal methods without explicitly passing classes or objescts
#                   except they have some special connection with the classes 
#                -  "@staticmethod" decorator is used.
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

    #1.
    @classmethod
    def set_inc(cls,inc):
        cls.inc=inc

    #2.
    @classmethod
    def deets(cls,emp_str):
        first,last,pay=emp_str.split('-')
        return cls(first,last,pay)
    
    #3. 
    @staticmethod
    def is_workingDay(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        else:
            return True

emp1 = Employee('Corey','Taylor',50000)

#1.
#Employee.set_inc(emp1,1.7) 
#emp1.set_inc(1.7)#regular method
Employee.set_inc(1.7)# equivalent to Employee.inc=1.7
print(Employee.inc)
print(emp1.inc)
print(emp1.pay)
emp1.apply_inc()
print(emp1.pay)


#2. Conventional Method 
str1='John-Dae-70000'
str2='Joe-Den-20000'
str3='Jane-Esten-40000'

first,last,pay=str1.split('-')
new_emp1=Employee(first,last,pay)
print(new_emp1.__dict__)

first,last,pay=str2.split('-')
new_emp2=Employee(first,last,pay)
print(new_emp2.__dict__)

# using class method 

temp=Employee.deets(str3)
print(temp.__dict__)



#3. 
import datetime
my_date = datetime.date(2016,7,10)
print(Employee.is_workingDay(my_date))