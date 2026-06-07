#container with most water
height = [1,8,6,2,5,4,8,3,7]
left=0
right=len(height)-1
max_value=0
while left<right:
    area=min(height[left],height[right])*(right-left)
    max_value=max(max_value,area)
    if height[left]<height[right]:
        left+=1
    else:
        right-=1
print(max_value)