# Given an integer x, return true if x is a palindrome, and false otherwise.
#palindrome
#method 1 (math)
x=int(input())
num=x
rev=0
while x>0:
    ld=x%10
    rev=rev*10+ld
    x//=10
if num==rev:
    print("true")
else:
    print('false')


#2.method2 (check half number)
x=int(input())
if x<0 or (x!=0 and x%10 ==0):
    print(False)
else:
    rev=0
    while x>rev:
        rev=rev*10+x%10
        x//=10
    if x==rev or x==rev//10:
        print(True)
    else:
        print(False)

