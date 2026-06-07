# n=int(input())
# exp=int(input())
# mon_power=[]
# bonus=[]
# for i in range(n):
#     mon_power.append(int(input()))
# for i in range(n):
#     bonus.append(int(input()))
# print(mon_power)
# print(bonus)
# a=[]
# ans=0
# for k in range(n):
#     a.append([mon_power[k],bonus[k]])
# a.sort()
# print(a)
# for i in a:
#     if exp<i[0]:
#         break
#     exp+=i[1]
#     ans+=1
# print(ans)


# main_list=[[100,50],[200,300],[150,200],[300,450],[120,180]]
# main_list.sort()
# print(main_list)
# print(main_list)


#3sum
nums = [-1,0,1,2,-1,-4]

seen = set()
n = len(nums)

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):

            if nums[i] + nums[j] + nums[k] == 0:

                val = sorted([nums[i], nums[j], nums[k]])

                seen.add(tuple(val))

print(seen)

nums = [-1,0,1,2,-1,-4]
nums.sort()
ans=[]
n=len(nums)
for i in range(n):
    if i>0 and nums[i]==nums[i-1]:
        continue
    left=i+1
    right=n-1
    while left<right:
        total = nums[i] + nums[left] + nums[right]
        if total==0:
            ans.append([nums[i], nums[left], nums[right]])
            left+=1
            right-=1
            while left<right and nums[left]==nums[left-1]:
                left+=1
            while left<right and nums[right]==nums[right+1]:
                right-=1
        elif total<0:
            left+=1
        else:
            right-=1
print(ans)
