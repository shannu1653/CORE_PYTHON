#check whether perfect suare or not
num=16
is_perfect=False
for x in range(1,num):
    if (x**2==num):
        is_perfect=True
        break
if is_perfect:
    print('it is a perfect square')
else : 
    print('it is not a perfect square')