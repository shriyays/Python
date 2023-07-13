# GENERATORS

# Advantage : does not store values in memory and gives better performance than lists.

#traditional way to code a function
def square_num(nums):
    res=[]
    for i in nums:
        res.append(i*i)
    return res

nums=[1,2,3,4,5]
print(square_num(nums))
for num in square_num(nums):
    print(num)



#using a generator
def square_num(nums):
    for i in nums:
        yield i*i

nums=[1,2,3,4,5]
print(square_num(nums))
for num in square_num(nums):
    print(num)



#List Comprehension
my_nums=[x*x for x in nums]
print(my_nums)
for num in my_nums:
    print(num)

#List Comprehension using a generator
my_nums=(x*x for x in nums)
print(my_nums)
print(list(my_nums))
for num in my_nums:
    print(num)