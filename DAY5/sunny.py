# num=int(input("enter a number: "))
# i=1
# while i*i<num+1:
#     i+=1
# if i*i==num+1:
#     print("sunny")
# else:
#     print("not sunny")



#armstrong number 
# num=input("Enter a number : ")
# sum=0
# temp=num
# n=len(num)
# while temp>0:
#     digit=temp%10
#     sum+=digit**n
#     temp//=10
# if sum==num:
#     print("Armstrong")
# else:
#     print("not Armstrong")

#armstrong number without converting str
    # num=int(input("Enter a number : "))
    # temp1=num
    # count=0
    # while temp1>0:
    #     digit1=temp1%10
    #     count+=1
    #     temp1//=10
    # sum=0
    # temp=num
    # while temp>0:
    #     digit=temp%10
    #     sum+=digit**count
    #     temp//=10
    # if sum==num:
    #     print("Armstrong")
    # else:
    #     print("not Armstrong")

#prime numbers
    # num=int(input("enter a number : "))
    # if num>1:
    #     for i in range(2,num):
    #         if num%i==0:
    #             print("not a prime")
    #             break
    #     else:
    #         print("prime")
    # else:
    #     print("invalid input")

num=int(input("enter a number : "))
sum=[]
i=0
if num>1:
        for i in range(2,num+6):
            if num%i==0:
                print("not")
                
                
        else:
            
            sum.append(str(i))
            
else:
    print("invalid input")
print(sum)


# num=int(input("Enter a number : "))
# org=num
# rev=0
# while num>0:
#      digit=num%10
#      rev =rev*10+digit
#      num=num//10
# if org==rev:
#      print("pali")
# else : 
#      print("not")
    

