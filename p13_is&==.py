#  "==" VS "is"


'''
"==" : checks for equality - compares values only
"is" : checks for identity - compares objects' memory locations to see if they are
        pointing to the same objects in memory or not.

'''

l1=[1,2,3,4,5]
l2=[1,2,4,5]
if l1==l2:
    print("True")
else:
    print("False")


l1=[1,2,3,4,5]
l2=[1,2,3,4,5]
if l1==l2:
    print("True")
else:
    print("False")


l1=[1,2,3,4,5]
l2=[1,2,3,4,5]
if l1 is l2:
    print("True")
else:
    print("False")


l2=l1
if l1 is l2:
    print("True")
else:
    print("False")
l1[0]=69
print(l1)
print(l2)

