#loops
# for x in range(10):
#     print(x)

# for x in range(2,10,5):
#     print(x)

# for x in range(2,10,3):
#     print("x")

# def function(y):
#     for x in range(1,11):
#      print(f"{y} X {x} = {y *x}")
# table = int(input("enter a table value : "))
# function(table)

# def squre(s):
#    for x in range(s):
#       print(f"{x} square is {x*x}")
# squre(11)


#print square if even else cube
# def evenodd():
#     for x in range(1,21):
#      if x & 1==0:
#       print(f"{x} square is {x**2}")
#     else:
#       print(f"{x} square is {x**3}")
# evenodd()

#print numbers 20 with specific conditions
#1.if num is divisible by 2 the fizz
#2.if num is divisible by 3 then buzz
#3.if num id divisible by 2 & 3 then buzz

# for i in range(1,21):
#   if i & 1==0 and i %3==0:
#     print(f"{i} is FIZZBUZZ")
#   elif i % 3==0:
#     print(f"{i} is BUZZ")
#   elif i & 1 ==0:
#     print(f"{i} is FIZZ")
#   else:
#     print(i)

def sum(n):
    list=0
    for i in range(1,sum):
        list +=i
    print(f"sum of first {sum} numbers is {list}")
range =int(input("Enter range : "))
sum(range)
    
    
list = 0
for i in range(1,11):
  list +=i*i 
print(list)