#Assignment - Math random module & keywords
#Generate 5 random floats between 0 and 1.
import random
for i in range(5):
    print(random.random())

#2.Dice roll simulator using random.randint.
print("please roll a dice")
while True:
    number=random.randint(1,6)
    print("your number",number)

    again=input('try a again-(y/n) : ')
    if again.lower()!="y":
        print("good bye")
        break

#3.Convert 90 degrees to radians.
import math
pi=3.14
degrees=int(input("Enter degrees :  "))
radians=int(degrees*(pi/180))
print(f"{degrees} are in radains is {radians}")
print(math.radians(degrees))#using math function

#4.Factorial of a user-given number
import math
number=int(input("enter a factorail number : "))
print(math.factorial(number))
count=number
sum=1
for i in range(number,0,-1):
    sum =sum*i
print(sum)

#5. Shuffle a list of 10 integers.
a=[1,2,3,4,5,6,7,8,9,10]
random.shuffle(a)
print(a)

# Intermediate:
# 1. Lottery draw of 6 unique numbers from 1 to 49.
import random
a=range(1,50)
print(random.sample(a,k=6))


#Approximate using Monte Carlo.
import random

# Number of random points to generate
num_points = 100000

inside_circle = 0

for _ in range(num_points):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    
    # Check if the point is inside the unit circle
    if x**2 + y**2 <= 1:
        inside_circle += 1

# Approximate value of π
approx_pi = 4 * inside_circle / num_points

print("Approximated value of π:", approx_pi)


#3. Calculate compound interest using math.pow.
import math

P = 10000
r = 0.06
n = 12  # compounded monthly
t = 18 / 12  # 18 months converted to years

# Calculate amount using math.pow
A = P * math.pow(1 + r / n, n * t)

# Compound interest
compound_interest = A - P

print("Amount:", A)
print("Compound Interest:", compound_interest)



# #Trigonometry calculator using degrees.
import math

# Input angle in degrees
angle_deg = float(input("Enter angle in degrees: "))

# Convert degrees to radians
angle_rad = math.radians(angle_deg)

# Calculate sine, cosine, and tangent
sine = math.sin(angle_rad)
cosine = math.cos(angle_rad)
tangent = math.tan(angle_rad)

print(f"sin({angle_deg}) = {sine}")
print(f"cos({angle_deg}) = {cosine}")
print(f"tan({angle_deg}) = {tangent}")









