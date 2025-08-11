#nested for loop
#create list of perfectsquare,neon,sunny using comprehension
#create list of revese string using comprehension

# ip=['hello','shannu','naveen','akhil']
def nested(num):
    list=[]
    for x in num:
        rev=" "
        for i in range(len(x)-1,-1,-1):
            # print(x[i])
            rev+=(x[i])
        list.append(rev)
    return list
op=[x for x in nested(['shannu','naveen','sathish','tharun','akhil'])]
print(op)

