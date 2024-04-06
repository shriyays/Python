# ITERABLES AND ITERATORS


#Iterable - anythhing that can be looped over - has the "__iter__()" function in its dir
#Iterator - object with a state that remembers where it is during an iteration 
#         - can only go forward, no going backward, resetting or making a copy
#Generator - for creating easy-to-read iterators - yeild a value instead of returning result
#          - stores the state and yields the next value when the generator is run again
#          - iterator as well - iter and next methods are created automatically



nums = [1,2,3] #list is an iterable but not an iterator
print(dir(nums))



'''
    Iterators get their next value using __next__(). 
    The __next__() is only applicable on iterators. Therefore, cannot be used on the list.
'''
print(iter(nums))
#print(next(nums)) #TypeError: 'list' object is not an iterator#

i_nums = iter(nums) #iterator
print(i_nums)
print(dir(i_nums))
print(next(i_nums))
print(next(i_nums))
print(next(i_nums))
#print(next(i_nums)) #StopIteration - exception error raised
print("")



''' 
    Therefore, when the for loop is used, what it does is that it calls the __iter__() 
    on an object and returns an iterator that we can loop over and handles the 
    StopIteration exception on its own.

'''
#for loop
i_nums = iter(nums)
while True:
    try:
        item=next(i_nums)
        print(item)
    except StopIteration:
        break
print("")

for num in nums : #num is an iterator
    print(num)




# copy of built-in range function

class MyRange:
    def __init__(self,start,end):
        self.value=start
        self.end=end

    #iterator
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.value>=self.end :
            raise StopIteration
        current=self.value
        self.value+=1
        return current
    

nums=MyRange(34,50)
print("")
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print("")
for num in nums:
    print(num)


#generator
def my_range(start,end):
    current=start
    while current<end:
        yield current
        current+=1

nums = my_range(1,10)
print("")
for num in nums:
    print(num)