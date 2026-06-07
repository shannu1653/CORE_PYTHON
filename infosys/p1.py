arr = [0,0,0]
k = 5

max_sum = 0

for i in range(k + 1):   # include k
    s = 0
    for j in arr:
        s += i ^ j
    if s > max_sum:
        max_sum = s

print(max_sum)

#Move Zeroes
nums=[0,1,0,3,0,12,0,15]
left=0
for right in range(len(nums)):
    if nums[right]:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
print(nums)