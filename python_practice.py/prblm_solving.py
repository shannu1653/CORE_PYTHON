#1.print even numbers in the range iof 1 to 20
# print(f"{numbers} " if numbers %2 ==0 else None for numbers in range(21) )

# print(*[number for number in range(1, 21) if number % 2 == 0])

# for i in range(1,21):
#     if (i%2==0):
#         print(i,end=" ")

#2.print odd numbers from 1 to 100
    # print(*[number for number in range(1, 101) if number % 2 != 0])

    # for i in range(1,101):
    #     if (i%2!=0):
    #         print(i,end=' ')

#3.print numbers from 1 to 50 divisible by 5
# print(*[number if number % 5 == 0 else None for number in range(1, 52)])
# print(*[number for number in range(1, 51) if number % 5 == 0])


#4.print multple 5 and 3 and both 3 and 5 range(1 ,50)
    # for i in range(1,51):
    #     if i%5==0 and i%3==0:
    #         print(f"{i} is multiple of 5 and 3")
    #     elif i%5==0:
    #         print(f"{i} is multiple of 5")
    #     elif i%3==0:
    #         print(f"{i} is multiple of 3")

    # for i in range(1, 51):
    #     print(f"{i} is multiple of 5 and 3" if i%15==0 else f"{i} is multiple of 5" if i%5==0 else f"{i} is multiple of 3" if i%3==0 else "", end="\n" if i%3==0 or i%5==0 else "")
    # [print(f"{i} is multiple of 5 and 3" if i%15==0 else f"{i} is multiple of 5" if i%5==0 else f"{i} is multiple of 3") for i in range(1, 51) if i%3==0 or i%5==0]

#5.find the number of numbers divisible ny both 3 and 7 from 1 to 100
    # hello=0
    # for i in range(1,101):
    #     if (i%3==0 and i%7==0):
    #         print(i)
    #         hello +=1
    # print(hello)

#6.print all upper case and lower case alphabets in a string,qlwogive the count of each type

    # str='ShaNMuKhaNavveNHello'
    # count1=0
    # count2=0
    # for char in str:
    #     if char.isupper():
    #         print(char,"is upper")
    #         count1 +=1
    #     else:
    #         print(char,"is lower")
    #         count2 +=1
    # print('we have',count1,'uppercase')
    # print('we have',count2,'lowercase')

# for a in range(1,101):
#     b=a**0.5
#     if b==int(b):
#         print(a)

string="madam"
a=print(string[len(string)-1:4:-1])
print(a)
if a==string:
    print("palindrome")
else:
    print("not palindrom")
