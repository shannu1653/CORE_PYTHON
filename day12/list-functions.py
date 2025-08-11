#list[]=list is a collection of different data types
#1.Append():to add an element at the end of the list.
list1=[1,2,3,4,4]
list1.append([634,343])#appends only one value else gives typeError
print(list1)

#2.extend() appends multiple value at a time
list1.extend([2,34,54]) 
print(list1)

#3.insert() -->add an element to a particular index
list2=[1,23,44,556,5667]
list2.insert(0,234343)#add but didnot remove original element
print(list2)

#4.replace()--> 





#5.remove() -->remove particular element
list2.remove(1)
print(list2)

#5.pop() -->remove last element in the list
#or remove an element specified position
list=[1,2,3,4,5,6,7]
list.pop()
print(list)

##Note: The pop() method returns removed value.**************

fruits = ['apple', 'banana', 'cherry']

x = fruits.pop(1)

print(x)


#6.count() -->to get the numbe of occurence of an element
list=[1,2,33,22,2,2,2,23,3,44444444,3]
print(list.count(2))

#7.clear():it removes all elements from the list
# list.clear()
# print(list)

#8.The copy() method returns a copy of the specified list.
#syntax-list.copy()
x=list.copy()
print(x)

#9.The index() method returns the position at the first occurrence of the specified value.
# Syntax
# list.index(elmnt, start, end)start	Optional. A number representing where to start the search
                               #end	    Optional. A number representing where to end the search
print(list.index(3))
print(list.index(3,9))#Note: The index() method only returns the first occurrence of the value.

#10.reverse() The reverse() method reverses the sorting order of the elements.
fruits = ['apple', 'banana', 'cherry']

fruits.reverse()

print(fruits)


#11.sort()  Sort the list alphabetically:
cars = ['Ford', 'BMWhffhf', 'Volvo']
cars.sort(reverse=True)
print(cars)
