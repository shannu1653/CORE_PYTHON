# #the graetest number
# num=(input("Enter a number : "))
# count=0
# for i in num:
#     if int(i)>count:
#         count=int(i)
# print(f"The greatest value is {count}")

for i in range(11, 10001):
    j = i
    num = 0
    num2 = 1
    while j != 0:
        temp = j % 10
        num = num + temp
        num2 = num2 * temp
        j = j // 10
    if num == num2:
        print(i)


# a="abaabaabba"
# list=''
# for i in a:
#     if i not in list:
#         list+=(i)
# print((list))

