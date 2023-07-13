#LOOPS

# for loop

list = [1,2,3,4,5]
for i in list :
    print(i)

for i in list:
    if i==3:
        print("found 3 at position",list.index(3),"!")
        break
    print(i)

for i in list:
    if i==3:
        print("found 3 at position",list.index(3),"!")
        continue
    print(i)

for i in list:
    for letter in "abc":
        print(i,letter)

for i in range(7):
    print(i)

for i in range(1,13): #start inclusive, end exclusive
    print(i)


# while loop
x=0
while x < 10 :
    if x == 5:
        break
    print(x)
    x+=1
    
    