#1.Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#Two Sum

#method 1 Bruteforce
'''arr=[2,7,11,15]
target=9
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==target:
            print([i,j])'''

#method 2 hashmap/complement
arr=[2,7,11,15]
target=9
seen={}
for i,j in enumerate(arr):
    complement=target-j
    if complement in seen:
        print([seen[complement],i])
    else:
        seen[j]=i