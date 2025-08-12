# #Star pattern
# for x in range(5):
#     str=""
#     for j in range(x+1):
#         str+="*"
#     print(str)

#number pattern(repeated)
for x in range(1,6):
    str3=0
    for j in range(x):
        str3=str3*10+x
    print(str3)

#number pattern
for x in range(1,6):
    str4=0
    for j in range(x+1):
        str4=str4*10+j
    print(str4)
# #asscii values  (repeated)
# for x in range(97,102):
#     str=""
#     for j in range(97,x+1):
#         str+=chr(x)
#     print(str)

# #ascci values not repeated(a-z)
# for x in range(97,123):
#     str=""
#     for j in range(97,x+1):
#         str+=chr(j)
#     print(str)

# str=""
# for x in "something":
#     str+=x
#     # for j in range(97,x+1):
#     #     str+=chr(j)
#     print(str)


name="something"
length=len(name)
for x in range(length,-1,-1):
    str1=""
    for j in range(x):
        str1+=name[j]
    print(str1)


for x in range(1,6):
    name1=''
    for j in range(1,x+1): 
        a=j*j
        name1+=str(a)
    print(name1)

# #reverse star pattern
# for x in range(5,0,-1):
#     str=""
#     for y in range(x):
#         str+="*"
#     print(str)

# #traingle
# rows=4
# for i in range(1,rows+1):
#     for j in range(rows-i):
#         print(" ",end=" ")
#     for k in range(i):
#         print("*",end=" ")
#     print()

# #pyramid
# rows=4
# for i in range(1,rows+1):
#     for j in range(rows-i):
#         print(" ",end="")
#     for k in range(i):
#         print("* ",end="")
#     print()

# Number pattern:
for i in range(1,6):
    str=0
    for j in range(i+1):
        str=str*10+j
    print(str)

# #5. Floyd's Triangle:
# rows=5
# number=1
# for i in range(1,rows+1):
#     for j in range(i):
#         print(number,end=" ")
#         number+=1
#     print()


# def prime(num):
#     for i in range(2,num):
#             for j in range(2,i):
#                 if (i%j==0):
#                     break
#             else:
#                 print(i,end=" ") 
                
# prime(101)  
       
# def prime(num):
#     is_prime=True
#     if (num<=1):
#         print('please give a number grater than 1')
#     else:
#          for i in range(2,num):
#                 if (num%i==0):
#                     is_prime=False
#                     break
#          if is_prime:
#                 return True        
#          else:
#                 return False 
# # prime(101)  
# result=[x for x in range(2,101) if prime(x)]       
# print("\n",result)


# #better version
# def prime(num):
#     for i in range(2,num):
#             for j in range(2,int(i**0.5)+1):
#                 if (i%j==0):
#                     break
#             else:
#                 print(i,end=" ") 
# prime(10001)