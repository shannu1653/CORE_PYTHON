#controll statements
#1.if statements
#1.1 wap grater than two numbers
a=33
b=45
print("A greater than B" if a>b else "B is greater than A")

#**INDETATION**(whitespace at the begining of a line)
a=33
b=200
if b>a:
    print("b is greater than a")#you will get an  error without space)

#2.Elif conditon-->if the previous condtion were not true,then try this condition
a=33
b=33
if b>a:
    print("b is greater than a")
elif a==b:
     print("a and b are equal")

#3.Else(anything which isn"t caught by the preceding condtions)
a=200
b=30
#using terinary style
print("b is greater than b" if b>a else "a and b are eual" if a==b else "a is greate than b")

#4.nested if(using is statements inside if statements)
x=41
if x>10:
    print("Above ten" )
    if x>20:
        print("Also above 20")
    else:
        print("but not above 20.")

x = 9
print("Above ten,\nand also above 20!" if x > 20 else "but not above 20.")

#5.the pass statement(if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.)
a=33
b=40
if a>b:
    pass