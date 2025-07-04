def name(first_name,last_name):
    print(f"hi {first_name} and bye {last_name}")
    print("just for joke")

a = input("enter your first name : ")
b = input("Enter your last name : ")

for i in range(3):
    name(a,b)


def greet(name):
    print(f"hi { name }")
greet("shannu")

#return value
def increament(number,by):
    return number + by
print(increament(5,2))

#default arguments
def increament(a , b , c = 1 ):
    return a + b + c
print(increament(1, 7))

#args,wait,what?
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total
print(multiply(2,3,4))

#**args
def save_user(**user):
    print(user)
save_user(id=1,name = 'shannu' ,age = 33)

#scope
message = "a"

def grat(name):
    message = "b"
grat("mosh")
print(message)


message = "a"
#global varible
def grat(name):
    global message
    message = "b"
grat("mosh")
print(message)

#fizzbuzz problem
def fizz_buzz(input):
    for input in range(100):
        if input % 3 ==0 and input % 5 == 0 :
            print("FIZZBUZZ")
        elif input % 3 ==0:
            print("FIZZ")
        elif input % 5 ==0 :
            print("BUZZ")
        else :
            print(input)
fizz_buzz(range)


def creat_name(first,last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last
full_name = creat_name("spongebob","squarepants")
print(full_name)


print('"value of pi:3.14"')   

num=float(input("enter digit"))
# print('"value for pi:',num,sep=" ",end='"')