# #data types
# #type: int, float, str, bool, list, dict, tuple, set
# #  Numbers: int, float, complex
# a = 10             # Integer
# b = 3.14           # Float
# c = 2 + 3j         # Complex number
# print("Numbers:", a, b, c)
# print("Types:", type(a), type(b), type(c))

# #  Type Conversion
# x = float(a)       # int to float
# y = int(b)         # float to int
# print("Converted:", x, y)

# #  Random Numbers
# import random
# print("Random Number (1–100):", random.randint(1, 100))

# #  Strings
# name = "Shanmukha"
# quote = 'He said "Python is fun!"'
# multi_line = """This is
# a multiline string"""
# print(name, quote)
# print("Upper:", name.upper())
# print("Sliced:", name[0:4])
# print("Contains 'shan'?", "shan" in name.lower())

# #  String Operations
# greeting = "Hello"
# target = "World"
# combined = greeting + " " + target
# formatted = f"{greeting}, {target}!"
# print("Concatenation:", combined)
# print("Formatted:", formatted)

# # String Methods
# s = "  hello Python  "
# print("Stripped:", s.strip())
# print("Replaced:", s.replace("Python", "World"))
# print("Split:", s.split())

# #  Escape Characters
# print("He said, \"Python is awesome!\"\nLet's code.")

# #  Booleans
# print("Is 10 > 5?", 10 > 5)
# print("bool(0):", bool(0))         # False
# print("bool('Python'):", bool("Python"))  # True

# #  Lists (ordered, changeable, duplicates allowed)
# print("==========================================")
# fruits = ["apple", "banana", "mango"]
# fruits.append("grape")         # Add item
# fruits[1] = "orange"           # Modify
# print("List:", fruits)
# fruits.remove("apple")         # Remove item
# print("Updated List:", fruits)

# #  Tuples (ordered, unchangeable, duplicates allowed)
# print("==========================================")
# colors = ("red", "green", "blue")
# print("Tuple:", colors)
# print("Access:", colors[0])
# # colors[1] = "yellow"   This would raise an error

# #  Unpack Tuple
# r, g, c = colors
# print("Unpacked:", r, g, c)

# #  Sets (unordered, no duplicates)
# print("====================================")
# letters = {"a", "b", "a", "c"}
# letters.add("d")
# print("Set:", letters)
# letters.remove("b")
# print("After Remove:", letters)

# #  Dictionaries (key-value pairs, ordered from Python 3.7+)
# person = {
#     "name": "Shan",
#     "age": 21,
#     "course": "Python"
# }
# print("Dictionary:", person)
# print("Name:", person["name"])
# person["age"] = 22               # Update
# person["city"] = "Hyderabad"     # Add
# del person["course"]             # Delete
# print("Updated Dictionary:", person)

# #  Nested Dictionary
# students = {
#     1: {"name": "A", "age": 20},
#     2: {"name": "B", "age": 21}
# }
# print("Nested Dictionary:", students[1]["name"])

# a='''
# i love my india,
# my brother name is shankar,
# my father name is ramu'''
# print(a)


# a=5
# b=2.5
# c='hello'
# d=[1,2,3,]
# e=(1,2)
# f={"a":1,"b":2}
# g={1,2,3}
# for i in [a,b,c,d,e,f,g]:
#     print(type(i))


# Demonstrate mutable vs immutable
# x=[1,2,3]
# y=x
# y.append(4)
# print(x)

# a="hi"
# b=a
# b=b,'there'
# print(a)

# # Q4. Create a dictionary to store student details
# student={'name':'ravi','age':20,'marks':85}
# print(student['name'],'scored',student['marks'],'marks')

# # Q5. Create a set and show uniqueness
# nums=[1,2,3,4,3,2,3]
# print(nums)
# nums1=set(nums)
# print(nums1)
# # print(nums)


# Q9. Demonstrate complex number
# z=2+3j
# print(z.real)
#  print(z.imag) 'it give floating values'

# Q10. Type conversion chaining
# x=10
# x=float(x)
# x=str(x)
# print(x,type(x))
# print(x+"hi")

# list=[2,3]
# for i in list:
#     fact=1
#     for j in range(1,i+1):
#         fact=fact*j
#     print(f"factorial of {i} : {fact}")


# list=['oreder','mutable','indexing','duplicates allowed','heterogeneous']
# dic={'name':'shannu'}
# dic1={'age':23}
# dic2={}
# for i in dic:
#     dic2[i]=dic[i]
# for j in dic1:
#     dic2[j]=dic1[j]
# print(dic2)

# name = "hello world example"
# name2 = name.split()
# print(name2)
# new_word = ""
# for i in name2:
#     if i != name2[-1]:
#         new_word += i.capitalize() + "_"
#     else:
#         new_word += i.capitalize()
# print(new_word)






# name = "hello world example"
# name2=""
# codtion=True
# for i in name:
#     if i==" ":
#         name2+="_"
#         codtion=True
#     else:
#         if codtion:
#             name2+=i.upper()
#             codtion=False
#         else:
#             name2+=i
# print(name2)


name="sHannU@4343&%@ABC"
small=""
capital=""
numbers=""
special=""
for i in name:
    if "a"<=i<="z":
        small+=i
    elif "A"<=i<="Z": 
        capital+=i
    elif "0"<=i<="9":
        numbers+=i
    else:
        special+=i
print(capital)   
print(numbers)  
print(special)
print(small)


    