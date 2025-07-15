#1.len() function
a="shannu"
count=0
for i in a:
    count+=1
print("without function",count) #without function

print("with function",len(a))#with function

#2.Type Casting
#int to float,string,complex
num=10
print(float(num))
print(str(num))
print(complex(num))

#str to int,float,complex
num="20"
print(int(num))
print(float(num))
print(complex(num))

# float to  int,str,complex
num=30.0
print(int(num))
print(str(num))#it gives only float value
print(complex(num))

# complex to only str
num=40+0j
# print(int(num))
# print(float(num))
print(str(num)) #it gives same value complex
val1=10
val2=20
print(complex(val1,val2))
print(complex(val1))
print(complex(val2))
val3=10+20j
print(val3.real)#gives real value in floating points
print(val3.imag)#gives imaginary value in flaoting points

# 2.Absolute()-->abs()It returns the distance of a value 0 to specific
a=10.23
print(abs(a))
b=3+4j
print(abs(b)) #it gives square root of a value

# 3.power()-->pow()It raised a value to the power of value passed next to it
print(pow(3,2))

# 4.divmod()-->it returns the coffitient and remainder of a division
a=10
b=5
print(divmod(a,b))

# 5.Round-->round gives nearest interger value to a specific number or decimal point
print(round(10.5)) #choose nearest even number in python
print(round(11.5))
print(round(9.6))
print(round(9.4))

#6.min() & max()
print(min(4,3,4,2,34,43,343,3,4))
print(max(3,32,3234,234,3,234,4,33,23,4,1))


