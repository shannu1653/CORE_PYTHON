#1.Check Even or odd
num=int(input("Enter a number : "))
print(f"{num} is even" if num & 1==0 else f"{num} is odd")

#2.Divisible by 5 but Not by 10
num=int(input("Enter a number : "))
print(f"{num} is divisible by 5 but not 10" if num %5==0 and num%10 !=0 else None)


#3.Biggest Among Two Numbers
num1=int(input("Enter number1 : "))
num2=int(input("Enter number2 : "))
print(f"Biggest is :{num1}" if num1>num2 else f"Biggest is : {num2}")

#4.Smallest Among Two Numbers
num1=int(input("Enter number1 : "))
num2=int(input("Enter number2 : "))
print(f"Smallest is :{num1}" if num1<num2 else f"Smallest is : {num2}")

#5.Divisible by 2,3 and 6
num=int(input("Enter a number : "))
print(f"{num} is divisible by 2,3,6" if num % 2==0 and num % 3==0 else f"{num} Not divisible by 2,3,6")

#6.Voting Eligibility
age=int(input("Enter your age : "))
print("Eligible to vote" if age>=18 else "NOt Eligible to vote" )

#7.Student Pass/Fail Based on All Subjects >= 35
maths=int(input("Enter your maths marks : "))
physics=int(input("Enter your physics marks : "))
chemistry=int(input("Enter your chemistry marks : "))
print("PASS" if maths>=35 and physics>=35 and chemistry>=35 else "FAIL")

#8.Student Pass if Passed Any one Subjects
maths=int(input("Enter your maths marks : "))
physics=int(input("Enter your physics marks : "))
chemistry=int(input("Enter your chemistry marks : "))
passed = 0
if maths >= 35:
    passed += 1
if physics >= 35:
    passed += 1
if chemistry >= 35:
    passed += 1
if passed >= 1:
    print("Student Passed")
else:
    print("Student Failed")

#9.Student Pass if Passed Any two Subjects
marks = (int(input(f"Subject {i+1}: ")) for i in range(3))
print("Student Passed" if sum(m >= 35 for m in marks) >= 2 else "Student Failed")


#10. Biggest Among Three Numbers
num1, num2, num3 = int(input("Enter num1: ")), int(input("Enter num2: ")), int(input("Enter num3: "))
print(f"{num1} is the biggest" if num1 > num2 and num1 > num3 else f"{num2} is the biggest" if num2 > num1 and num2 > num3 else f"{num3} is the biggest")

#11. Smallest Among Three Numbers
num1, num2, num3 = int(input("Enter num1: ")), int(input("Enter num2: ")), int(input("Enter num3: "))
print(f"{num1} is the Smallest" if num1 < num2 and num1 < num3 else f"{num2} is the Smallest" if num2 < num1 and num2 < num3 else f"{num3} is the Smallest")

#12. Perfect Square or Not
square_num = int(input("Enter a number : "))
value=square_num**0.5
print(f"{square_num} is a perect Squre" if value==int(value) else "not a perfect Suare")

#13. Cars Required for Members (Max 5 per car)
members=int(input("Members count : "))
if members % 5==0:
    cars=members//5
else:
    cars = (members +4)//5
print(f"{cars} cars needed")

#14.Second Biggest Among Three Numbers
a,b,c=int(input("Enter number1 : ")),int(input("Enter number2 : ")),int(input("Enter number3 : "))
if (a<=b and a>=c or a<=c and a>=b) :
    print(f"{a} is Second biggest number")
elif (b<=c and b>=a or b<=a and b>=c) :
    print(f"{b} is Second biggest number")
else:
     print(f"{c} is Second biggest number")


#15.Leap Year or Not
year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")