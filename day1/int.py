#problem sum of digits
n=123
total=0
while n>0:
    total += n % 10
    n//=10
print(total)

#reverse a num
n=123
rev=0
while n>0:
    rev=rev*10+n%10
    n//=10
print(rev)

#palindrome
n=12321
rev=0
while n>rev:
    rev=rev*10+n%10
    n//=10
if rev==n or n==rev//10:
    print('palindrome')
        

#prime check
n=9
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        print('Not a Prime')
        break
else:
    print("prime")

#armstrong
n=153
temp=n
count=0
while temp>0:
    count+=1
    temp//=10
temp=n
total=0

while temp>0:
    ld=temp%10
    total +=ld**count
    temp//=10
if total==n:
    print("Armstrong")
else:
    print("Not A Armstrong")

#gcd
a,b=12,18
c=a
big=0
n=1
while c>0:
    if a%n==0 and b%n==0:
        big=n
    n+=1
    c-=1
print(big)

#gcd euclid
a,b=12,18
while b!=0:
    a,b=b,a%b
print(a)

#gcd on n inputs

nums=[12,18,34,24]
result=nums[0]
for num in nums[1:]:
    while num!=0:
        result, num = num, result % num
print(result)

#lcm of two numbers
a, b = 12, 18

if a == 0 or b == 0:
    print(0)
else:
    x, y = a, b
    while y != 0:
        x, y = y, x % y

    print((a * b) // x)

#lcm of multiple numbers
nums=[12,18,24]
result=nums[0]
for i in range(1,len(nums)):
    a=result
    b=nums[i]
    while b!=0:
        a,b=b,a % b
    gcd = a
    result=(result*nums[i])//gcd
print(result)

#*****************#Count number of divisors 12*****************************************
n=12
count=0
i=1
while i*i<=n:
    if n%i==0:
        if i==n//i:
            count+=1
        else:
            count+=2
    i+=1
print(count)

# “Sum of Divisors”?
n=12
value=0
i=1
while i*i<=n:
    if n%i==0:
        if i==n//i:
            value+=i
        else:
            value+=i
            value+=n//i
    i+=1
print(value)


#Perfect Number?
n=28
if n<=1:
    print('Not A Perfect Number')
else:
    total = 1
    i=2
    while i*i<=n:
        if n%i==0:
            if i==n//i:
                total +=i
            else:
                total +=i+(n//i)
        i+=1
    if total==n:
        print('Perfect Number')
    else:
        print("Not A Perfect Number")

#Check if number is Prime using √n
n=8
if n<2:
    print('Not A Prime')
else:
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            print("Not A Prime Number")
            break
    else:
        print("Prime Number")
