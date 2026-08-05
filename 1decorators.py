#1.Example decorator
def decorator(func):
    def wrapper():
        print("Program Started")
        func()
        print("Program finished")
    return wrapper
@decorator
def greet():
    pass
greet()

#2.Create a decorator that checks whether a number is positive before calling a function.
def check_positive(func):
    def wrapper(n):
        if n>0:
            print("Positive")
            func(n)
        else:
            print("Negative")
    return wrapper
@check_positive
def num(n):
    print(n)
num(5)
num(-20)

#3.Create a decorator that prints the execution time of a function.
import time
def cal_excution_time(func):
    def wrapper():
        start=time.time()
        func()
        end=time.time()
        excution_time=end-start
        print(f"Execution Time: {excution_time:.4f} seconds")
    return wrapper

@cal_excution_time
def work():
    time.sleep(2)
work()

#4.Create a decorator that counts how many times a function is called.
def count_func_time(func):
    count=0
    def wrapper():
        nonlocal count
        func()
        count +=1
        print(f"Funnction called {count} times")
    return wrapper
@count_func_time
def sample():
    print("Hello")
sample()
sample()
sample()

#5.Create a decorator that logs the function name before execution.
def function_log(func):
    def wrapper():
        print(f"Calling fucntion : {func.__name__}")
        func()
    return wrapper
@function_log
def greet():
    print("Hello")

@function_log
def add():
    print(5+5)

greet()
add()

#Problem #6**********: Create a decorator that only allows a function to run if the user is "admin".************
def admin_only(func):
    def wrapper(user):
        if user=="admin":
            print("Access Granted")
            func(user)
        else:
            print("Access Denied")
    return wrapper

@admin_only
def delete_user(user):
    print(f"{user} deleted a user")
delete_user("admin")
print()
delete_user("shanmukha")