#Python Loops in Sequence Types, Problems 
#1.conditional Statements
#1.Check even or odd
num=int(input("Enter a number : "))
print(f"The given number {num} is even " if num & 1==0 else f"The given number {num} is odd")

#2.Age group Classifier
age=int(input("Enter your age : "))
print("Child" if age<13 else "Teen" if age<=20 else "Adult")

#3.Check if a number is positiv,negative,or zero
number=int(input("Enter a number : "))
print("Positive" if number>0 else "Zero" if number==0 else "Negative")

#4.Divisibility Checker
#(check if a number is divisible by bothh 3 and 5)
number=int(input("Enter a number : "))
print(f"{number} is divisible by both 3 and 5" if number %3==0 and number%5==0 else "not divisible both 3 and 5")
 
#5.Find Largest of Two Numbers
num1=int(input("Enter  number 1 : "))
num2=int(input("Enter  number 2 : "))
print(f"{num1} is Largest Number" if num1>num2 else f"{num2} is Largest Number")

#**** .strip() removes accidental spaces from user input.******

#6.Traingle Validity checker
#Give three sides(eg:s1=15, s2=10, s3=23), 
#check if they can form a triangle (that is, sum of any two sides > third side).
side1,side2,side3=int(input("Enter side1 : ")),int(input("Enter side2 : ")),int(input("Enter side3 : "))
print("Traigle" if side2+side3>side1 and side1+side3>side2 and side1+side2>side3 else "Not a traingle")

##for loop with sequential data
#1.Print each character of a string
str=input("Enter a string_name : ")
for char in str:
    print(char,end=" " \
    "")
    


#2.Sum of first 10 natural numbers
sum=0
for num in range(1,11):
    sum+=num
print(f"Sum of first 10 natural numbers is {sum}")

# 3.Print even numbers from 1 to 10
for num in range(1,11):
    if num & 1==0:
        print(num,end=" ")

# 4.Print elements in a list
list=['pen','pencil','eraser']
list2=[]
for elements in list:
    list2.append(elements)
print(list2)

# 5.Print common elements in two list
list1=['shannu','naveen','nagaraj','tharun']
list2=['shannu','hemanth','nagaraj','prashanth']
common=[]
for i in list1:
    if i in list2:
        common.append(i)
print(common)

# 6.Print all elements in a set
my_set={'apple','bannna','cherry'}
for i in my_set:
    print(i)

#7.Count how many items are in a set using a loop
colors = {"red", "blue", "green", "yellow"}
count=0
for items in colors:
    count+=1
print(count)

#8.Print all keys and values in a dictionary
person = {"name": "Alice", "age": 25, "city": "Delhi"}
for keys,value in  person.items():
    print(keys, ':' , value)

#9.Count how many values in a dictionary are greater than 50
scores = {"math": 45, "english": 55, "science": 80, "history": 40}
count=0
for value in scores.values():
    if value>50:
        count+=1
print(f"Total {count} values are greater than 50")

#10.Create a new dictionary with only items where the value is even
data = {"a": 1, "b": 4, "c": 6, "d": 3}
new_dictionary={}
for  keys,values in data.items():
    if values &1 ==0:
        new_dictionary[keys]=values
print(new_dictionary)

