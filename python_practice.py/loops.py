# num=123444557668
# value=0
# while(num>0):
#     ld=num%10
#     print(ld,end=" ")
#     num=num//10
#     value+=1
# print(value)

# num=123444557668
# num1=str(num)
# count=0
# for i in num1:
#     count+=1
# print(count)

# num=123444557668
# num1=str(num)
# count=0
# for i in num1:
#     count +=int(i)
# print(count)

# num=125
# num1=str(num)
# value=0
# for i in num1:
#     value+=(int(i)**2)
# print(value)


# num=123444557668
# value=0
# value1=0
# while(num>0):
#     ld=num%10
#     print(ld,end='')
#     value +=1
#     num=num//10
#     value1+=ld

# # print(value)
# print(value)
# print(value1)

# num=125
# value=0
# while(num>0):
#     ld=num%10
#     # print(ld,end=" ")
#     num=num//10
#     # print(ld,end=" ")
#     print(ld,end=" ")
#     value+=ld
# print(value)

#reverse a num using while loop witout cpnverting into string
# num=123456
# rev=0
# while(num>0):
#     ld=num%10
#     rev=rev*10+ld
#     num =num//10
# print(rev)



# #check palindrome or not
num= 12345
num2=num
rev=0
while(num>0):
    ld=num%10
    rev=rev*10+ld
    num =num//10
print(rev)
if num2==rev:
    print("palindrome")
else:
    print('not a palindrome')


