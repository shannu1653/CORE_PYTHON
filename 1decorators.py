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