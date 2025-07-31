
# Practise discussed topics first and the
#1. Write a program to check input string is palindrome or not using while loop

str=input("Enter a string : ")
str2=""
lenght=len(str)-1
while lenght!=-1:
    str2+=str[lenght]
    lenght -=1
# print(str2)
if str==str2:
    print("palindrome")
else:
    print("Not a palindrome")

#2. Write a program to reverse a number without converting into string

num= 1223243423221
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