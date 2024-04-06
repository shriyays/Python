# READ

#opening files using context manager "with" : automatically closes fiels without 'f.close()'
file="test.txt"
with open('test.txt','r') as f:
    f_contents=f.read()
    print(f_contents)

with open('test.txt','r') as f:
    f2=f.readlines()
    print(f2)

with open('test.txt','r') as f:
    f3=f.readline()
    print(f3)
    f3=f.readline()
    print(f3)

#no memory issues will be encountered 
with open('test.txt','r') as f:
    for line in f:
        print(line,end=' ')#prints everything by looping line by line

#memory might get full for large files
    f_contents=f.read()
    print(f_contents,"\n","\n",'\n',"\n",end=' ') #prints everything all at once

with open('test.txt','r') as f:
#first 100 characters only get printed
    f_contents=f.read(100)
    print(f_contents,end=' ')
    f_contents=f.read(100)
    print(f_contents,end=' ')


#looping through 100 characters at a time until the end of the file
with open(file,'r') as f:
    size = 100
    f_contents = f.read(size)
    while len(f_contents)>0 :
        print(f_contents,end='')
        f_contents = f.read(size)

#no. of characters read
with open(file,'r') as f:
    
    f_contents = f.read(10)
    print(f.tell())
    #to set file pointer position to beginning of the file
    f.seek(0)
    f_contents = f.read(10)
    print(f_contents)
    #to set the file pointer postion to the specified number
    f.seek(51)
    f_contents = f.read(10)
    print(f_contents)





    