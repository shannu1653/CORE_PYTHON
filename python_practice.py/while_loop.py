# y=1
# while (y<=10):
#     print(y)
#     y+=1

# flashsale=1
# while(flashsale):
#      print("dp shopping with more offers")
    

# number=0
# while(number%2==0 and number<=20)  :
#     print(number)
#     number+=2 #whenver condition fail,loop will exit at moment

# num=1
# while(num <=20):
#     if (num &1==0 ):
#         print(num)
#     num +=1

# str="madam"
# # print(str)
# op=""
# for char in range(len(str)-1,-1,-1):
#     op+=str[char]
# print(op)
# if (op==str):
#     print("pallindrom")
# else:
#     print("not pallindrom")


#using while loop check string is palindrom or not

# str1=input("Enter string name : ")
# value=len(str1)-1
# list=""
# while value!=-1:
#     list+=str1[value]
#     value -=1
# if str1==list:
#     print("palindrome")   
# else:
#     print("not palindrome")

#reverse a num without convrting onto string using while loop
# number=1234
# number2=number
# rev=0
# while number>0:
#     td=number%10
#     rev=rev*10+td
#     number=number //10
# print(rev)


# #Fibonacci Sequence
# sequence=""
# count=0
# for i in range(20):
#     count+=i
#     sequence +=str(count)
# print(sequence)


# numbers=int(input("Enter a list of numbers : "))
# print(numbers)


#asscending order
# arr = [1,2,6,3,4,8,4,9]
# for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#         if arr[i] > arr[j]:
#             arr[i],arr[j]=arr[j],arr[i]
# print(arr)




            


number=8096087857
num=[]
while number>0:
    td=number%10
    num.append(td)
    number=number//10
new_dict={}
count=0
for i in num:
    if i in new_dict:
        count +=1
    else:
        new_dict[i]=count
print(new_dict)



# #fibonccci series
# number=int(input('Enter a number : '))
# a=0
# b=1
# count=0
# while(count<number):
#     print(a," ",end='')
#     temp=a+b
#     a=b
#     b=temp
#     count+=1