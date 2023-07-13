#LISTS 

# 1. Lists - sequential data - mutable - sqaure brackets

print("LISTS")
courses = ["hist",'math','phy','cs']
print(courses)
print(len(courses))
print(courses[0])
print(courses[-1])
print(courses[-2])
print(courses[:3])
print(courses[1:3]) #start - inclusive & end - exclusive

print("Lists' methods")
courses.append("art")
print(courses)

courses = ["hist",'math','phy','cs']
courses.insert(0,"Art")
print(courses)

courses = ["hist",'math','phy','cs']
extra=['art',"pe"]
courses.insert(0,extra)
print(courses)

courses = ["hist",'math','phy','cs']
courses.extend(extra)
print(courses)

courses.remove("math")
print(courses)

popped=courses.pop()
print(courses)
print(popped)

courses.reverse()
print(courses)

courses.sort()
print(courses)

courses.sort(reverse=True)
print(courses)

num=[2,4,5,1,3]
num.sort()
print(num)
num.sort(reverse=True)
print(num)

courses = ["hist",'math','phy','cs']
print(sorted(courses))
print(courses)

print(min(num))
print(max(num))
print(sum(num))
print(courses.index("cs"))
#print(courses.index('art'))
print("art" in courses)

for course in courses:
    print(course)

for index, course in enumerate(courses):
    print(index,course)

for index, course in enumerate (courses, start=1):
    print(index, course)

course_st='-'.join(courses)
print(course_st)
new_list=course_st.split('-')
print(new_list)

#creating empty list with built-in class 
empty_list=[]
empty_list=list()
