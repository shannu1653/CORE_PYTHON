#import keyword:to import modules from python,so that we can use the functions of that specific module in our program
import math
#Numeric function
# import math
#1.ceil function -->it rounds up to the closet integer value.
print(math.ceil(4.2))
print(math.ceil(4.5))

#2.floor function-->it rounds to the closet integer value
print(math.floor(4.2))
print(math.floor(4.6))

#3.truncate()-->trunc()-it removes decimal part of a float number
print(math.trunc(234.34))
print(math.trunc(0.34))

#4.factorial -->it returns the factorial of a value passed to it.
print(math.factorial(5))
fact=1
for i in range(1,6):
    fact*=i
print(fact)

#5.constants
print((math.pi))
print(math.inf)#infinite
print(math.nan)#using data cleaning in excel
print(math.e)