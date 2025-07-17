
#comprehension --> is a combination of  iteration,filtration(optional)  and expresion.
#1.list comprehension 
# 2.tuple comprehension 
# 3.sets cimprehension 
# 4.dictionat=ry comprehenison

# op=[ x+2 for x in range(1,10) if x%2==0]
# print(op)

# op=[ x for x in range(1,10)]
# print(op)

# #create alist of suares of numbers from 1 to 20 using comprhension
# op=[ x**2 for x in range(1,10)]
# print(op)


# #upper()--> it changes to lower case to upper case
# list=['kiran','harish','harish','shannu']
# op=[x.upper() for x in list]
# print(op)

# #lower()--> it changes  upper case lower case
# list=['KIRAN', 'HARISH', 'HARISH', 'SHANNU']
# op=[x.lower() for x in list]
# print(op)

# #suare of even numbers from 10 to 30
# op=[ x**2 for x in range(10,31) if x%2==0]
# print(op)


# list=['kiran','harish','harish','shannu']
# op=[x.upper() for x in list if len(x)&1==0]
# print(op)

def vowel(ip):
    count=0
    for x in ip:
        if x in ['a','e','o','i','u']:
            count+=1
    if (count & 1==0):
        return True
    else:
        return False
list=['kiran','harish','harish','shannu']
op=[x.upper() for x in list if vowel(x) ]
print(op)