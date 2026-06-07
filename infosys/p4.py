nums = [2,0,2,1,1,0]
nums2=[]
count_zero=0
count_one=0
count_two=0
for i in nums:
    if i==0:
        count_zero+=1
    elif i==1:
        count_one+=1
    else:
        count_two+=1
for i in range(count_two):
    nums2.append(0)
for i in range(count_one):
    nums2.append(1)
for i in range(count_two):
    nums2.append(2)
print(nums2)