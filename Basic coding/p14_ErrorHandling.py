# ERROR HANDLING

#1.
try:
    f=open("random.txt") # - file does not exist
except Exception:
    print("Sorry , the file does not exist.")

#2.
try:
    f=open("random.txt")
    var=bad_var

except FileNotFoundError:
    print("sorry")

except Exception:
    print("Sorry")


#3.
try:
    f=open("random.txt")
    var=bad_var

except FileNotFoundError as e:
    print(e)

except Exception:
    print("Sorry")


#4.
try:
    f=open("test.txt") #correct file
    
except Exception as e:
    print("Sorry")

else:
    print(f.read())
    f.close()
finally:
    print("Done")


#5.
try:
    f=open("corrupt_file.txt")
    if f.name=="corrupt_file.txt":
        raise Exception
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("Finally")