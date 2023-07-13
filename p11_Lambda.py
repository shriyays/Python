# LAMBDA FUNCTION

# - anonymous temporary function - one line function
# This function can have any number of arguments but only one expression, 
# which is evaluated and returned.
# syntax : "function_name = lambda arguments : returned_expression"

#1.
add5 = lambda x : x + 5
print(add5(7))

#2.
square = lambda x : x*x
print(square(4))

#3.
get_tens = lambda x : int(x/10)%10
print(get_tens(2424))

#4. Sorting a list of tuples using lambda
list1 = [('eggs',23),('honey',234),('carrots',2334)]
list1.sort(key=lambda x : x[0])
print(list1)
list1.sort(key=lambda x : x[1])
print(list1)

#5. Sorting dictionaries using lambda
import pprint as pp 
#pretty printer module : The pprint module in Python is a utility module that you can
#                        use to print data structures in a readable, pretty way.

list1 = [{'make':"Ford",'model':"Focus","year":2019},
        {'make':"Toyota",'model':"X","year":2020}
        ]
list1 = sorted(list1,key = lambda x : x['year'])
pp.pprint(list1)
print(list1)


#6. Filtering integers in lists
list1=[1,2,3,4,5,6,7]
odds=lambda x : x % 2 == 1
evens = lambda x : x % 2 == 0
listo=list(filter(odds,list1))
liste=list(filter(evens,list1))
print(listo,liste,sep='\n')


#7. 
list1=[1,2,3,4,5,6]
list2=list(map(lambda x : x ** 2,list1))
print(list2)

#8.
starts_withJ = lambda x : x.startswith('J')
print(starts_withJ("JOEY"))

#9.
wordb4 = lambda s,w : s.split()[s.split().index(w)-1] if w in s else None
sentence = 'Four Score and seven years ago'
print(wordb4(sentence,'seven'))

#10.
import datetime
now = datetime.datetime.now()
print(now)
year=lambda x:x.year
print(year(now))

#11.
def func(f,val):
    return f(val)

f=lambda x : x**3
print(f(12))
print(func(f,5))

