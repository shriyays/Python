# MAP

# - takes a list of items and maps the given funciton to each individual item

#squaring numbers
list1=[1,2,3]
slist=list(map(lambda x : x**2,list1))
print(list1)
print(slist)

#changing case
values = ['abc','sdf','sdadf']
llist = list(map(lambda x : x.upper(),values))
print(values,llist,sep='\n')




# FILTER

# - filters out contents based on specified conditions

#values greater than 3
nums=[1,2,3,4,5,6]
print(list(filter(lambda x : x>3,nums)))




# REDUCE

# - takes an existing function, applies it cumulatively to all the items in an iterable,
#  and generate a single final value.

nums = [1,2,3,4,5,6,7]
from functools import reduce
print(reduce(lambda x,y:x+y,nums))

