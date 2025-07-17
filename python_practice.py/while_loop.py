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

str="madam"
# print(str)
op=""
for char in range(len(str)-1,-1,-1):
    op+=str[char]
print(op)
if (op==str):
    print("pallindrom")
else:
    print("not pallindrom")


#using while loop check string is palindrom or not
#reverse a num without convrting onto string using while loop

str1=input("Enter string name : ")
value=len(str1)-1
list=""
while value!=-1:
    list+=str1[value]
    value -=1
if str1==list:
    print("palindrome")   
else:
    print("not palindrome")



    

    


