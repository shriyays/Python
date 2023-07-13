#DICTIONARIES 

student={'name':'John','age':52}
print(student)
print(student['name'])
print(student['age'])
#print(student['phone']) - KeyError: 'phone'

print(student.get('name'))
print(student.get('phone'))
print(student.get('phone',"not found"))
print(student.get('phone'))
print(student.get('email'))

student['phone']='555-555'
print(student.get('phone',"not found"))

student['phone']='555-666'
student['name']="Jane"
print(student)

student.update({'name':"whatever","age":0,"phone":"who cares","email":"idk"})
print(student)

del student['email']
print(student)

age = student.pop('age')
print(student)
print(age)

print(len(student))

print(student.keys())

print(student.values())

print(student.items())

for key in student:
    print(key)

for key, value in student.items():
    print(key,":", value)

#print(student.name) - AttributeError: 'dict' object has no attribute 'name'