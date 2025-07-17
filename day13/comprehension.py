
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

# def vowel(ip):
#     count=0
#     for x in ip:
#         if x in ['a','e','o','i','u']:
#             count+=1
#     if (count & 1==0):
#         return True
#     else:
#         return False
# list=['kiran','harish','harish','shannu']
# op=[x.upper()  for x in list if vowel(x) ]
# print(op)

# num=28
# sum=0
# for x in range(1,num):
#     if num %x==0:
#         sum+=x
# if (sum==num):
#     print("perfect number")
# else: 
#     print("not a perfect number")



# def perfect(value):
#     sum=0
#     for x in range(1,value):
#         if value %x==0:
#          sum+=x
#     if (sum==value):
#      return True
#     else: 
#       return False

# op=[x for x in range(1,50) if perfect(x)]
# print(op)

#create a list of armstrong numbers from 100 to 1000
#do research how to generate tuple comprehension


# #armstrong number
# def armstrong(number):
#     number2=number
#     count=0
#     while (number>0):
#      num=number%10
#      count+=1
#      number=number//10
#     temp=number2
#     count2=0
#     while number2>0:
#      num=number2%10
#      count2+=num**count
#      number2=number2//10 
#     if count2==temp:
#         return True
#     else:
#         return False

# op=[x for x in range(100,1000) if armstrong(x)]
# print(f"Armstrong numbers from range(100,1000) are {op}")


for i in range(11,10001):
    j=i
    count=0
    count2=1
    while j>0:
        temp =j%10
        count+=temp
        count2 =count2*temp
        j=j//10
    if count ==count2:
        print(i)







