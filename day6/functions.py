#general program

def function_name(name,age):
    print(f"HI {name}")
    print(f"{name} are {age} old")
function_name("shannu",22)

#types of arguments
#default,positional,keyword,orbitary

#1.positional
def function_name(name,age):
    print(f"HI {name}")
    print(f"{name} are {age} old")
function_name("shanmukh",22)

#2.keyword
def function_name(name,dept = "hi"):
    print(f"hi {name} ")
    print(f"Are you from {dept} department")
function_name(dept = "helo ",name="shannu")

#3.mixture of postional & keyword arguments

def function_name(name ,dept):
    print(f"HI {name}")
    print(f"Are you from {dept}")
function_name(1,dept = "shannu")

#4.Default arguments
def function_name(name ,subject,dept ="cs"):
    print(f"HI {name}")
    print(f"Are you from {dept} and teaching {subject} subject")
function_name(1,"python")

#5.arguments(using *(astrisk))
#positional
def add(*numbers):
    c = 0
    for i in numbers:
        c = c + i
    print(f"The sum of numbers {c}")
add(5,6,7,8)
add(1,2,3,4,5,6,7,8,9,10)

#6.arguments using(**Kwargs)
def add (**numbers):
    print(numbers)
add(name= "shannu",age=71)

def add(*numbers):
    c = 0
    print(numbers)
    for i in numbers:
        c = c + i
    print(f"The sum is {c}")
add(1,2)

#7.**Kwargs Examples
def info_persion(*args,**kwargs):
    # print(kwargs)
    for i,j in kwargs.items():
        print(i,j)
    print(args)
info_persion(1,2,3,name="shannu",age= 27)
print("\u20B9")


#8. Excersice (multiplication)
def multiplication(*numbers):
    c = 1
    for i in numbers:
        c = c * i
    print(f"The multiplication of all numbers is {c}")
multiplication(1,2,34)