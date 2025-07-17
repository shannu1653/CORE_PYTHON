# a,b,c,d,e=1,2,3,4,5
# print(a,b,c,d,e)

#1.print 5 lines using single print
# print("shannu \nnaveen \nnagaraj \nprashanth")

#2.print multiline quote using """ """
# print('''hello
      

#        navven are 
#       u ok''')


#3.print "python" 5 times using * operator 
    # print("python\n"*5) 
    # print("python  "*5) 
#4.print \n and \t
    # print("\\t \\n")

#5.use sep and end in print()
    # print("10k","nice","inhyd",sep=" -- ",end=" bye")

#6.print table formate using tabs \n and \t are know as tabs
    # print("name\tage\tschool_name") 
    # print("shanmu\t23\tmaharajahs")
    # print("navven\t22\tarts college")
    # print("nagrau\t25\tmahatma")

#7.print a formated string using f-string
# a ="formated_string"
# print(f"{a}")
# print("\u20B9")

# marks = (int(input(f"Subject {i+1}: ")) for i in range(3))
# # print("Student Passed" if sum(m >= 35 for m in marks) >= 2 else "Student Failed")
# num=(int(input(f"num {i+1}: "))for i in range(3))

#10. Biggest Among Three Numbers
# print(f"Biggest is {max(int(input()), int(input()), int(input()))}")

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# biggest = max(a, b, c)
# print(f"{biggest} is the biggest")

# square_num = int(input("Enter a number : "))
# value=square_num**0.5
# print(f"{square_num} is a perect Squre" if value==int(value) else "not a perfect Suare")

# members=int(input("Members count : "))
# if members % 5==0:
#     cars=members//5
# else:
#     cars = (members + 4)//5
# print(f"{cars} cars needed")

# a,b,c=int(input("Enter number1 : ")),int(input("Enter number2 : ")),int(input("Enter number3 : "))
# if (a<=b and a>=c or a<=c and a>=b) :
#     print(f"{a} is Second biggest number")
# elif (b<=c and b>=a or b<=a and b>=c) :
#     print(f"{b} is Second biggest number")
# else:
#      print(f"{c} is Second biggest number")


# #15.Leap Year or Not
# year = int(input("Enter a year: "))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f"{year} is a leap year")
#         else:
#             print(f"{year} is not a leap year")
#     else:
#         print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")

st=10
while st<20:
    print("hi")
    st+=1
