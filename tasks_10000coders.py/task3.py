#terinary operations and lamda functions
x=20
def show():
    x=5
    print(x)
show()
print(x) #output 5 and 20,x=5 is local varible and x=20 global varible

def outer():
    x=30
    def inner():
        print(x)
    inner()
outer()
#output 30 because x=30 local varible only on outer() function

x='global'
def outer():
    x='outer'
    def inner():
        x='inner'
    inner()
    print('outer:',x)
outer()
print('global:',x)
'''output outer:outer ,global:global beacuse outer is 
local varible to outer() function and global is x'''