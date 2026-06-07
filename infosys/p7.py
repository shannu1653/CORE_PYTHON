#max_sub array with distinct intgers and k length
nums=[1,5,4,2,4,6]
k=3
freq={}
window_sum=0
max_sum=0
for i in range(k):
    window_sum+=nums[i]
    freq[nums[i]]=freq.get(nums[i],0)+1
if len(freq)==k:
    max_sum=window_sum

for j in range(k,len(nums)):
    window_sum+=nums[j]
    freq[nums[j]]=freq.get(nums[j],0)+1
    window_sum-=nums[j-k]
    freq[nums[j-k]]-=1
    if freq[nums[j-k]]==0:
        del freq[nums[j-k]]
    
    if len(freq)==k:
        max_sum=max(max_sum,window_sum)
print(max_sum)