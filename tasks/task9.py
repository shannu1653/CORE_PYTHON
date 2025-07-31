# #pattern 1
for x in range(102,97,-1):
    str=""
    for j in range(97,x):
        str+=chr(j)
    print(str)

#pattern 2
lenth=0
for x in range(97,102):
    lenth +=1
for x in range(97,102):
    value=""
    value+=chr(x)*lenth
    lenth-=1
    print(value)

#pattern 3
lenth=0
for x in range(97,102):
    lenth +=1
for x in range(101,96,-1):
    value=""
    value+=chr(x)*lenth
    lenth-=1
    print(value)

#right angled traingle
for i in range(5):
    rev=""
    for j in range(i+1):
        rev=rev+"*"
    print(rev)

#Inverted right angle traingle
for i in range(5,-1,-1):
    rev=""
    for j in range(i):
        rev+="*"
    print(rev)

#traingle
rows=4
for i in range(1,rows+1):
    for j in range(rows-i):
        print(" ",end=" ")
    for k in range(i):
        print("*",end=" ")
    print()

#pyramid
rows=4
for i in range(1,rows+1):
    for j in range(rows-i):
        print(" ",end="")
    for k in range(i):
        print("* ",end="")
    print()

# Number pattern:
for i in range(1,6):
    str=0
    for j in range(i+1):
        str=str*10+j
    print(str)

#5. Floyd's Triangle:
rows=5
number=1
for i in range(1,rows+1):
    for j in range(i):
        print(number,end=" ")
        number+=1
    print()



