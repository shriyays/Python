#CONDITIONAL STATEMENTS AND BOOLEANS

#IF , ELIF , ELSE

lang = "py"
if lang == "py":
    print("python")
elif lang == "java":
    print("java")
else : 
    print("meh")

#PYTHON DOES NOT HAVE SWITCH STATEMENT 

#BOOLEAN - and , or , not

user="Admin"; login = True

if user == 'Admin' and login :
    print('admin page')
else : 
    print("L")

#DIFFERENCE BETWEEN "==" AND "is"

a = [1,2,3]
b = [1,2,3]

print(a==b) #CHECKS VALUE
print(a is b) #CHECKS MEMORY LOCATION
print(id(a),id(b))
