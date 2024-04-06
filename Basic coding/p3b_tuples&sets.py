#TUPLES

# 2. Tuples - immutable lists - paranthesis

print("TUPLES\n")
t1 = ('h','m','p','cs')
t2=t1
print(t1,'\n',t2)

l1 = ["hist",'math','phy','cs']
l2=l1
print(l1,'\n',l2)

#t1[0]='art'
print(t1,'\n',t2)

l1[0]="art"
print(l1,'\n',l2)

#creating empty tuple with built-in class 
empty_tuple=()
empty_tuple=tuple()
print(empty_tuple)



#SETS 

# 3. SETS - list of unordered values - no dupes - '{}' used - sets are used for membership tests ,they run more efficiently than lists or tuples
# - sets can quickly determine what value they either share or dont with other sets
print("SETS")
set = {'hist','math','phy','cs'}
print(set)
print(set)

set = {'hist','math','phy','cs','math'}
print(set)
print("math" in set)

#functions 
cs_courses={'h','m','p','cs'}
art_courses={'h','m','a','cs'}

print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))

#creating empty set with built-in class 
#empty_set={}
empty_set=set()
print(empty_set)