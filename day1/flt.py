'''#float-a float is a data type  is used to store decimal(fractional) numbers
x=0.5
z=10.5
m=0.0
print(type(m))

#1.convert to flaot
a=5
print(a,type(a))
b=float(a)
print(b,type(b))

#2.float operations
#2.1 Addition
print(2.5+4.2)
#2.2 Subtraction
print(9.3 - 3.2)

#***********SEE REEAL VALUES **********
print(format(2.4, '.20f'))
print(format(30.0,'.20f'))

#2.3 multiplication
print(2.0 * 3.0)

#2.4 division 
print(5/2)

#2.5 FLOOR DIVISION
print(5.5 % 2)

#2.6 modulus
print(5.5 % 3,'modulus')

#3 FLOAT FUNCTION METHODS
#3.1 ROUND()
print(round(3.1234, 2),'round')

#3.2 abs() --> Gives positive values
print(abs(-4.3))

#3.3 pow() --> it gives power
print(pow(2,3))

print(float('inf'))##it give infinity values
print(float('-inf')) ## it gives infinity negitive values
print(float('nan')) ## not a number

#PRECISION PROBLEM
print(0.1+0.2)
print(round(0.1+0.2,3))#fix 1 precession value using round function
from decimal import Decimal
print(Decimal('0.1') + Decimal('0.2')) #fix 2 precission value using decimal

#Comparison problem
print(0.1 + 0.2 == 0.3)  #it gives False Due to Precsion
#use isclose
import math
print(math.isclose(0.1+0.2,0.3))#***********imp


#FLOAT TO FRACTION
print((0.5).as_integer_ratio())
print((100.50).as_integer_ratio())

#it checks it can be covert integer or not
print((5.0).is_integer()) #it gives true
print((5.5).is_integer()) #it gives False

#******hex() and fromhex() is used to low level debugging currenetly not mandatory


'''

#give second largest
arr=[2,4,5,61,113,90]
first=second=float('-inf')
for i in arr:
    if i > first:
        second = first
        first = i       
    elif i > second:
        second = i
print(second)


#third largest
arr=[2,4,5,61,113,90]
first=second=third=float('-inf')
for i in arr:
    if i > first:
        third = second
        second = first
        first = i
    elif i > second:
        third = second
        second = i
    elif i > third:
        third = i
print(third)