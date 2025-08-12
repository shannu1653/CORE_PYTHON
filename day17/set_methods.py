#set functions:-it can be sequence,unorder,mutable
#note : by default we cannot declare a empty set, the empty brackets {} are considered as dictionary by pythonin

#in  order to declare a empty set we use built in set functions.

set1={1,2,3,}
set2=set()
print(type(set2))

#add() :- adds an element to the existing set
set1.add(6)
print(set1)
set1.add(5)
print(set1)

#update() :-
set1.update([8,9],(10,11),{13,14})
print(set1)

#remove() :- removes an element from the set,raises an error if given value not found
set1.remove(14)
print(set1)

#discard() :-removes an element from the set,does not raises error if the value not found 
set1.remove(150)#it gives  key error
set1.discard(150)
print(set1)