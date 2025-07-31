#Python Number Function - Based Problems
#problems on int
#1.Convert a floating -point number to an integer
print(int(4.89))
#2.Convert a string "7" to int and multiply it by 5
a="7"
integ=int(a)
print(integ,integ*5)

#problems on float()
#3.Conver an integer input to flaot
a=int(input("Enter a integer value : "))
print(float(a))
#4.Convert string '3.1415' to flaot and add 1
a='3.1415'
b=float(a)
print(b,b+1)

#problems on complex()
#5.Create a complex number from real and imaginary inputs
a=20
b=30
print(complex(a,b))
#6.Return square of a complex number using complex()
c=20+30j
square=c**2
print(f"suare of {c} is {square}")

#problems in round()
#7.Round 6.72849 to 2 decimal places
print(round(6.72849,2))
#8.Round user-input float to nearest integer.
num=float(input("Enter a number(flaot) : "))
print(round(num))

#Problems on min() and max()
#9.Find min and max from Find min and max from [2, 5, 1, 9, -3, 6].
list=[2, 5, 1, 9, -3, 6]
print(max(list))
print(min(list))
#10.Find the largest of three numbers using max().
number=34324,343,32
print(max(number))
#11.Find alphabetically first name from ["Zara", "Bob", "Alice"].
list=["Zara", "Bob", "Alice"]
print(min(list))


#Problems on pow()
#12. Find 2 ** 5 using pow().
print(pow(2,5))
#13. Get base and exponent from user, return result.
base=int(input("Enter a number for base : "))
exponent=int(input("Enter a number for exponent : "))
print(pow(base,exponent))
#14. Use pow(x, y, z) to find (x**y) % z with inputs x=2, y=3, z=5.
x,y,z=2,3,5
print(pow(x,y)%z)

#Problems on divmod()
#15.Use divmod() for 23 divided by 5.
print(divmod(23,5))
#16.Write function to return quotient and remainder.
def divm(quotient,remainder):
    return divmod(quotient,remainder)
q,r=divm(10,2)
print("quotient",q)
print("reminder",r)
#17. Convert number to binary using repeated divmod(num, 2).
num = 4
binary = ''

while num > 0:
    num, rem = divmod(num, 2)
    binary = str(rem) + binary

print("Binary is:", binary)

#problems on abs()
#18.Print absolute value of a user-input number
number=float(input("Enter a number : "))
print(abs(number))
#19.Get absolute difference between two numbers.
a = 15
b = 22
diff = abs(a - b)
print("Absolute difference:", diff)
#20.compute manhattan distance from (x,y) to origin
x = 3
y = 4
distance = abs(x) + abs(y)
print("Manhattan distance to origin:", distance)

#Bonus Practice
#21.Multiply  two string inputs as integers
a = input("Enter first number: ")
b = input("Enter second number: ")
result = int(a) * int(b)
print("Product:", result)
#22.Round pow(5,3)/7 to 3 decimal places
num=(pow(5,3)/7)
print(round(num,3))
#23.Print largest absolute value from [-1,-1,3,7]
a=[-1,-1,3,7]
num=0
for i in a:
    if abs(i)>num:
        num=abs(i)
print("The greatest absolute value",num)
#24.Round user float input,then use as wxponent for 2
num=float(input("Enter a number(floating value) : "))
num2=int(num)
num3=round(num2)
print(num3**2)