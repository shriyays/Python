#BUILT IN MODULES

#1.
import random 
courses = ["History","Math","English","Art"]
random_course = random.choice(courses)
print(random_course)

#2.
import math
rads=math.radians(90)
print(rads)
print(math.sin(rads))

#3.
import datetime
import calendar
today = datetime.date.today()
print(today)

print(calendar.isleap(2017))
print(calendar.isleap(2020))
print(calendar.isleap(2021))

#4.
import os
print(os.getcwd())

print(os.__file__)

#5.  comic
import antigravity
