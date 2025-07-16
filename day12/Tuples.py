#tuple() -->immutable
#1.count--.returns the number odf occurences of an element in a tuple
tuple1=(1,2,3,3,4,5,6)
print(tuple1.count(1))

#2.index -->index value passed it
print(tuple1.index(3))
print(tuple1.index(3,3))

#3.packing --> combining multiple value into a single value
# unpacking --> 
data=1,2,3,4,5
print(data) #it gives value in a tuple

# unpacking --> Accesing each individula elements from a collection of data
#if you don't the  number of values in a tuple we use arbitraty varibles which are denoted by *.
a,*b,c,d=data
print(a)
print(b)
print(c)
print(d)
