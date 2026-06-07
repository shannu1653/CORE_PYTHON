#two sum if array is sorted
numbers=[1,2,4,5,6,7]
target=9
left=0
right=len(numbers)-1
while left<right:
    sum=numbers[left]+numbers[right]
    if sum==target:
        print([left,right])
        break
    elif sum>target:
        right-=1
    else:
        left+=1
