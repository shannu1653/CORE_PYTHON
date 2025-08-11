#dictionary methods -->it stroes data in the form of keys and values
dict1={'name':'sathish','course':"python","city":'hyderabad'}
#1.length():-it return the number of key-value pairs
print(len(dict1))
print(dict1)
print(dict1.keys())#it returns the list of all keys with dictionary
print(dict1.values())#it returns the list of all values with dictionary
print(dict1.items())

#2.update():-update a dictionary with another
dict2={'phone.number':12345667890,'address':'karimnagar'}
dict1.update(dict2)
print(dict1)

#3.clear():it removes all the values an empty
dict1.clear()
print(dict1)
print(dict2.clear())
