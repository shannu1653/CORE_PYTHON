# #1.check whether perfect square or not
# num=23
# is_perfect=False
# for x in range(1,num):
#     if (x*x==num): #or if x**2==num
#         is_perfect=True
#         break
# if is_perfect:
#     print('it is a perfect square')
# else : 
#     print('it is not a perfect square')

# #2.sunny number-->num+1==square
# num=24
# is_sunny=False
# for x in range(1,num):
#     if (x*x==num+1):
#         is_sunny=True
#         break
# if is_sunny:
#     print("is is sunny number")
# else:
#     print("it is not sunny number")

#3.neon number (9-->81--<8+1=9>)neon number

number = 9
square = number ** 2
sum_of_digits = 0

while square > 0:
    digit = square % 10
    sum_of_digits += digit
    square = square // 10

if sum_of_digits == number:
    print("The number is a Neon number")
else:
    print("Not a Neon number")



# #4.prime number
# def prime(num):
#     is_prime=True
#     if (num<=1):
#         print('please give a number grater than 1')
#     else:
#         for i in range(2,num):
#             if (num%i==0):
#                 is_prime=False
#                 break
#         if (is_prime):
#             return True
#         else:
#            return False

# op=[x for x in range(2,51) if prime(x)]
# print(op)

# op=tuple(x for x in range(2,51) if prime(x)) #tuple comprehwnsion using tuple generator
# print(op)

# op={x for x in range(2,51) if prime(x)}  #set comprenwnsion
# print(op)

# op=[x for x in range(2,51) if prime(x)]
# print(op)

#mostly used list and set


