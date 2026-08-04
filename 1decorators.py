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
    