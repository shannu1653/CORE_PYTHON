#1.crete a list perfect square using list comprehension
def square(num):
    is_perfect=False
    for x in range(1,num):
        if (x*x==num): #or if x**2==num
            is_perfect=True
            break
    if is_perfect:
        return True
    else : 
       return False
result=[x for x in range(1,101) if square(x)]
print(f"Perfect squars of range(1,100) is {result}")

# 2.Create a list of  neon numbers using list comprehension
def neon(num):
    square = num ** 2
    sum = 0
    while square > 0:
        ld = square % 10
        sum = sum + ld
        square = square // 10
    if sum == num:
        return True
    else:
        return False

result = [x for x in range(1, 1000) if neon(x)]
print(f"Neon numbers in range(1,100): {result}")
#There are only three neon numbers: 0, 1, and 9

#3.Create a list of sunny numbers using list comprehension
def sunny(num):
    is_sunny=False
    for x in range(1,num):
        if (x*x==num+1):
            is_sunny=True
            break
    if is_sunny:
        return True
    else:
        return False
result = [x for x in range(1,101) if sunny(x)]
print(f"Sunny numbers in range(1,100): {result}")

#4.create list of revese string using comprehension
def nested(num):
    list=[]
    for x in num:
        rev=" "
        for i in range(len(x)-1,-1,-1):
            # print(x[i])
            rev+=(x[i])
        list.append(rev)
    return list
op=[x for x in nested(['shannu','naveen','sathish','tharun','akhil'])]
print(op)

