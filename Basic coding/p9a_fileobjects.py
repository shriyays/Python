# FILE OBJECTS - READING AND WRITING TO FILES 

file="test.txt"

#opening file to read (by default)
f=open(file)

#opening file to read only
f=open(file,'r')

#opening file for writing only
f=open(file,"w")

#opening file for appendind only
f=open(file,'a')

#opening file to read and write
f=open(file,'r+')

#closing the file
f.close()

print(f.name)
print(f.mode)

