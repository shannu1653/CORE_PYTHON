#operators
#1.Arithmetic
#2.Comparison
#3.Logical
#4.Bitwise
#5.Assignment
#6.identity
#7.membership


#1.ARITHMETIC OPERATORS(+,-,*,/,%,//,**)
a=10
b=5
print(a+b)
print(a-b)
print(a*b)
print(a/b) #-->quotient
print(a%b) #-->remainder
print(a//b) #-->gives quotient by ignoring floating points
print(a**b)

#2.COMPARISION OPERATORS(==,!=,>,<,>=,<=)
a=5
print(a==5)
print(a!=5)
print(a>5)
print(a<5)
print(a>=5)
print(a<=5)


#3.LOGICAL OPERATORS(and,or,not)#Truth Table
print("3.LOGICAL OPERATORS")
a=5
b=4
c=True
d=False
print(a<5 and b==4)
print(a<=5 and b==4)
print(a<5 or b==4)
print(not(a))
print(not(c))
print(not(d))

#4.ASSIGNMENT OPERATOR(=,-=,+=,*=,/=,%=,**=,&=,|=,^=,>>=,<<=,:=)
print("4.ASSIGNMENT OPERATOR")
x=5
print(x)
x +=3
print(x)
x-=3
print(x) #5
x*=3
print(x) #15
x /=3
print(x) #5.0
x %=3
print(x) #2.0
x=10
x//=3
print(x) #3
x**=2
print(x) #9
x&=3
print(x)#1
x =10
x|=5
print(x)#15
x^=3
print(x)#12
x >>=2
print(x)#3
x<<=2
print(x)#12
print(x:=3)#3

#5.IDENTITY OPERATOR (is,not)#checks id same or not
print('5.IDENTITY OPERATOR')
print("hello")

a=6
