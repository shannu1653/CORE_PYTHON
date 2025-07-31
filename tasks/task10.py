#armstrong number using while loop
number=123
number2=number
count=0
while (number>0):
    count+=1
    number=number//10
temp=number2
count2=0
while number2>0:
    num=number2%10
    count2+=num**count
    number2=number2//10 
if count2==temp:
        print("armstrong")
else:
        print("Not armstrong")

#2.Check what is neon number and sunny number
number = 9
square = number ** 2
sum = 0

while square > 0:
    ld = square % 10
    sum = sum + ld
    square = square // 10

if sum == number:
    print("The number is a Neon number")
else:
    print("Not a Neon number")


#3.sunny number
num = int(input("Enter a number: "))
next_num = num + 1

i = 1
is_perfect_square = False

while i * i <= next_num:
    if i * i == next_num:
        is_perfect_square = True
        break
    i += 1

if is_perfect_square:
    print(f"{num} is a Sunny number")
else:
    print(f"{num} is not a Sunny number")
