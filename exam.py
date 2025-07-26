# #the graetest number
# num=(input("Enter a number : "))
# count=0
# for i in num:
#     if int(i)>count:
#         count=int(i)
# print(f"The greatest value is {count}")

# for i in range(11, 10001):
#     j = i
#     num = 0
#     num2 = 1
#     while j != 0:
#         temp = j % 10
#         num = num + temp
#         num2 = num2 * temp
#         j = j // 10
#     if num == num2:
#         print(i)


# a="abaabaabba"
# list=''
# for i in a:
#     if i not in list:
#         list+=(i)
# print((list))



number = ("153 21 136 44 234").split()

result = []  # empty list to collect sorted numbers

for i in number:
    number2 = list(i)  # convert string to list so we can swap
    length = len(number2)
    for j in range(length):
        min_index = j
        for x in range(j + 1, length):
            if number2[x] < number2[min_index]:  # find the smallest digit
                min_index = x
        number2[j], number2[min_index] = number2[min_index], number2[j]
    sorted_number = ''.join(number2)
    result.append(sorted_number)  # add to result list

print(result)

