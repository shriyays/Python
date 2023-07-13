# WRITE 

file="test2.txt" 

with open(file,"r") as f:
    f.read()
    #f.write("test") - io.UnsupportedOperation: not writable

with open(file,"w") as f: 
    #overwrites existing text the first time it is accessed
    f.write("test file 2 ")
    #gets appended
    f.write("test") 
    f.write("test")

    f.seek(0)
    #overwrites "test file 2"
    f.write("test file 3")
    #overwrites as it goes
    f.write("TEST")
    #overwrites "T"
    f.seek(0)
    f.write("R")

#for each line it makes a copy in the new file
with open(file,"r") as rf:
    with open("copy2.txt","w") as wf:
        for line in rf:
            wf.write(line)


#copying an image
'''
with open("cute.jpg",'r') as rf:
    with open("copy.jpg",'w') as wf:
        for line in rf:
            break
            #wf.write(line) - UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff 
            # in position 0: invalid start byte
            # Binary mode is needed , it is in texxt mode
'''
#binary mode
with open("cute.jpg",'rb') as rf:
    with open("copy.jpg",'wb') as wf:
        for line in rf:
            wf.write(line)


with open("cute.jpg",'rb') as rf:
    with open("copy2.jpg","wb") as wf:
        chunk_size = 4096
        rf_chunk=rf.read(chunk_size)
        while len(rf_chunk)>0:
            wf.write(rf_chunk)
            rf_chunk=rf.read(chunk_size)
