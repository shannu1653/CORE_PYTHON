import random
#1.random
    # print(random.random())#it returns 0.0 to 1.0

#2.uniform -->
    # print(random.uniform(10,20))

#3.randint()
    # print(random.randint(10,20))

#4.choice():returns a random element from a sequence
    # a=[1,2,3,4,5,6,7,8,9,10]
    # print(random.choice(a))

#5.choices():returns a sub sequences of elements from a sequence with a specific range.
    # a=[1,2,3,4,5,6,7,8,9,10]
    # print(random.choices(a ,k=5))

#6.sample():reeturns a random subsequence of unique elements from a sequence with a specified range.
    # a=range(91)
    # print(random.sample(a ,k=90))

#7.shuffle()
    # a=[1,2,3,4,5,5,6,7,8,9]
    # random.shuffle(a)
    # print(a)