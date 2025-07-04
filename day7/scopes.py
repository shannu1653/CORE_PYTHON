#enclosed to local
def func1():
    x=5
    def funct2():
          nonlocal x
          x=10
    funct2()
    print(x)
func1()

