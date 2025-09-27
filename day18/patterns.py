# list=['a','b','c','c','a',"b"]
# dict_1={}
# for i in list:
#     if (i in dict_1):
#         dict_1[i]+=1
#     else:
#         dict_1[i]=1
# print(dict_1)


# list="banana"
# dict_1={}
# for i in list:
#     if (i in dict_1):
#         dict_1[i]+=1
#     else:
#         dict_1[i]=1
# print(dict_1)


num=int(input("Enter a number : "))
for i in range(num+1,0,1):
    list=[]
    for j in range(1,i):
        list+=[j*j]
    print(*list)