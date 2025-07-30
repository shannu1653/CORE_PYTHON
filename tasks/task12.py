# #1.Add all elements of a list.
# list1=[]
# list1.extend([1,2,3,44,5,6])
# print(list1)

# #2.Find max and min in a list
# print(f"the maximum number of a list {max(list1)}")
 
#  #min a list
# print(f"the maximum number of a list {min(list1)}")

# #3.Count even and odd numbers in a list
# even=0
# odd=0
# for i in list1:
#     if i & 1==0:
#         even+=1
#     else:
#         odd+=1
# print(f"The count of even numbers in a list1 is  {even}")
# print(f"The count of odd numbers in a list1 is {odd}")

# #4.Reverse a list without usinf reverse()
# list1=[1,2,3,4,5,6,7]
# rev=[]
# for i in range(len(list1)-1,-1,-1):
#     rev.append(list1[i])
# print(rev)

# #5.Remove duplicates from list
# list1=[1,1,1,2,3,4,5,6,7,6,4,6,9]
# new_list=[]
# for i in list1:
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)

# #6.Sort s list of strings by lenth
# names=["shannu",'navven','prashanth','hanuman']
# names1=["shannu",'navven','prashanth','hanuman']
# names.sort()
# print(names)#alphabetically
# names1.sort(key=len)
# print(names1)#lenth

# #7.Find the second largest number in the list.
list1=[1,2,3,4,5,6,7,6,7,8,10,100,101]
unique_set=list(set(list1))
unique_set.sort()
print(unique_set)

#8.Find sum of all nested list elements
nested_list = [1, [2, 3], [4, [5, 6]], 7]
#ask to sir

#9.Checks if two list are equal
list1=[1,2,3,4]
list2=[1,2,3,4]
if list1==list2:
    print("Equal")

#10.Merge two lists and sort them
list1=[1,2,3,4]
list2=[5,23,33,64]
mixed_list=list1+list2
mixed_list.sort()
print(mixed_list)


#11.Comvert tuple to list and back
tuple1 = (3, 2, 3, 5, 2, 4, 5)

# Convert tuple to list
list1 = list(tuple1)
print("List:", list1)

# Convert list back to tuple
tuple2 = tuple(list1)
print("Tuple:", tuple2)


#12.Check if the tuple contains a value
if 5 in tuple2:
    print("yes")

#13.Unpack a tuple into variables
tuple1=(1,2,3,4,5)
a,b,c,*d=tuple1
print(a)
print(b)
print(c)
print(d)

#14.Creat a list of squares using comprehension
squres=[x*x for x in range(1,21) ]
print(squres)


#15.Count how many times a number appears in list
list1=[1,1,2,3,4,5,5,4,3,2,3,3,4]
for i in set(list1) :
    count=list1.count(i) 
    print(f"{i} - {count}")

#or 
list1 = [1,1,2,3,4,5,5,4,3,2,3,3,4]
count_dict = {}

for i in list1:
    if i in count_dict:
        count_dict[i] += 1
    else:
        count_dict[i] = 1

for num, count in count_dict.items():
    print(f"{num} - {count}")

#16. Find index of element in tuple.
tuple1=(3,343,2,3,55,2,34,5)
print(tuple1.index(55))

#17. Slice a tuple from index 1 to 3.
my_tuple = (10, 20, 30, 40, 50)

sliced_tuple = my_tuple[1:3]

print(sliced_tuple)

#18.Replace element in list with another
list1 = [1,1,2,3,4,5,5,4,3,2,3,3,4]
index=list1.index(5)
list1[index]=123
print(list1)

#19. Filter only strings from mixed lists.
mixed_list=[1,2,4,5,'g','r',4,5,'k']
for i in mixed_list:
    if isinstance(i,str):
        print(i)

#20. Take input of the list from the user and print sum.
list2=input("Enter a list of number : ").split()
list3=[int(x) for x in list2]
sum=0
for x in list3:
    sum+=x
print(sum)