def add(a,b):
    c = a+b
    return c
print(f"The sum of two numbers are {add(5,7)}")

#Example for title Heading
def name(f_name,l_name):
    formated_name =f_name.title()
    formattd_name= l_name.title()
    return f"{formated_name} {formattd_name}"
arguments = (name("shannu","penta"))
print(arguments)

#return multiple values
import statistics
def mean_mode_median(list1):
    return statistics.mean(list1),statistics.median(list1),statistics.mode(list1)
a,b,c = mean_mode_median([1,2,3,4,5,6,7,8])
print(f"mean is {a}\n median is {b}\n mode is {c} ")

#multiple return in single function

def add(a,b):
    if a == 0 and b == 0 :
        return "You have entered zero for both variables"
    else : 
        return a+b
var1 = int(input("Enter first varible : \n "))
var2 = int(input("Enter second varible : \n "))
result = add(var1,var2)
print(result)

#Exercise 25(month and leap year)
 
def leap_year(year):
    if year %4==0:
        if year%100==0:
            if year%400 ==0 :
                return True
            else:
                return False
        else:
            return True
    else :
        return False
def days_in_month(year,month):
    days_list = [31,28,31,30,31,30,31,31,30,31,30,31]
    if leap_year(year) and month ==2:
        return 29
    else:
        return days_list[month-1]
        

year = int(input("Enter a year : "))
month = int(input("Enter your month : "))
days = days_in_month(year,month)
print(days)

#print vs return
def fun1(x):
    return x+1
def fun2(a,b):
    return a+b
output = fun2(4,6)
output1 = fun1(output)
print(output1)