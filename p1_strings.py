#STRINGS

msg = 'python'
print(msg)

msg = "wahjda"
print(msg)

msg = 'Bob\'s world'
print(msg)

msg = '''so like
uhmmmm'''
print(msg)


#Length of a string
message = 'hello world'
print(len(message))

#indexing
print(message[0])
print(message[10])
#print(message[11])

#slicing - [start inclusive : end exclusive]
print(message[0:5])
print(message[:5])
print(message[6:])

#String Methods

print(message.lower())
print(message.upper())

print(message.count("hell"))
print(message.count('l'))

print(message.find("world"))

print(message.replace("world","universe"))

print(message)


#CONCATENATION
greet="hello"
name="Jae"
message=greet+name
print(message)

message=greet+','+name+'. Welcome!'
print(message)

message="{},{}. Welcome!".format(greet,name)
print(message)

message=f'{greet},{name}.Welcome!'
print(message)

print(dir(str)) # list of string methords will be displayed
#print(help(str))
#print(help(str.lower))



