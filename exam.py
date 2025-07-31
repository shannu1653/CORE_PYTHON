# #the graetest number
# num=(input("Enter a number : "))
# count=0
# for i in num:
#     if int(i)>count:
#         count=int(i)
# print(f"The greatest value is {count}")

# for i in range(11, 10001):
#     j = i
#     num = 0
#     num2 = 1
#     while j != 0:
#         temp = j % 10
#         num = num + temp
#         num2 = num2 * temp
#         j = j // 10
#     if num == num2:
#         print(i)


# a="abaabaabba"
# lst=''
# for i in a:
#     if i not in lst:
#         lst+=(i)
# print((lst))



# number = ("153 21 136 44 234").split()
# result = []
# for i in number:
#     number2 = list(i)
#     length = len(number2)
#     for j in range(length):
#         min_index = j
#         for x in range(j+1, length):
#             if number2[x] < number2[min_index]:
#                 min_index = x
#         number2[j], number2[min_index] = number2[min_index], number2[j]
#     sorted_number = ''.join(number2)
#     result.append(sorted_number)
# print(result)


# def is_prime(number):
#     if number==2:
#         return True
#     else:
#         for i in range(2,number):
#             if number%i==0:
#                 return False
#             else :
#                 return i
# print(is_prime(int(input("Enter a number : "))))


# def is_prime(number):
#     if number==2:
#         return True
#     else:
#         for i in range(2,number):
#             if number%i==0:
#                 return False
#             else :
#                 return True
# c=0
# for i in range(2,11):
#     if  is_prime(i):
#         c+=1
# print(c)

# n1='111'
# n2='100'
# sum=0
# j=0
# for i in range(len(n1)-1,-1,-1):
#     sum +=int(n1[i])*(2**j)
#     j+=1
# k=0   
# for i in range(len(n2)-1,-1,-1):
#     sum +=int(n2[i])*(2**k)
#     k+=1
# a=str(bin(sum))
# print(a)
# print(a[2:])


# name="sraaavan"
# name2=''
# count=-1
# for i in name:
#     if name2[count] ==name2[count+1] :
#         continue
#     else:
#         name2+=i
#     count+=1
# print(name2)

# s='sraaavan'
# res=s[0]
# c=1
# for i in range(1,len(s)):
#     if s[i]==s[i-1]:
#         c+=1
#         if c<3:
#             res +=s[i]
#     else:
#             c=1
#             res+=s[i]
# print(res)


# amount=100
# total_choclets=amount
# w=amount
# while w>=3:
#     e=w//3
#     total_choclets+=e
#     w=e+e%3
# print(total_choclets)