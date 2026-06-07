arr=[1,2,3]
first=0
second=len(arr)-1
while first<second:
    arr[first],arr[second]=arr[second],arr[first]
    first+=1
    second -=1
print(arr)
