#data types
#type: int, float, str, bool, list, dict, tuple, set
#  Numbers: int, float, complex
a = 10             # Integer
b = 3.14           # Float
c = 2 + 3j         # Complex number
print("Numbers:", a, b, c)
print("Types:", type(a), type(b), type(c))

#  Type Conversion
x = float(a)       # int to float
y = int(b)         # float to int
print("Converted:", x, y)

#  Random Numbers
import random
print("Random Number (1–100):", random.randint(1, 100))

#  Strings
name = "Shanmukha"
quote = 'He said "Python is fun!"'
multi_line = """This is
a multiline string"""
print(name, quote)
print("Upper:", name.upper())
print("Sliced:", name[0:4])
print("Contains 'shan'?", "shan" in name.lower())

#  String Operations
greeting = "Hello"
target = "World"
combined = greeting + " " + target
formatted = f"{greeting}, {target}!"
print("Concatenation:", combined)
print("Formatted:", formatted)

# String Methods
s = "  hello Python  "
print("Stripped:", s.strip())
print("Replaced:", s.replace("Python", "World"))
print("Split:", s.split())

#  Escape Characters
print("He said, \"Python is awesome!\"\nLet's code.")

#  Booleans
print("Is 10 > 5?", 10 > 5)
print("bool(0):", bool(0))         # False
print("bool('Python'):", bool("Python"))  # True

#  Lists (ordered, changeable, duplicates allowed)
print("==========================================")
fruits = ["apple", "banana", "mango"]
fruits.append("grape")         # Add item
fruits[1] = "orange"           # Modify
print("List:", fruits)
fruits.remove("apple")         # Remove item
print("Updated List:", fruits)

#  Tuples (ordered, unchangeable, duplicates allowed)
print("==========================================")
colors = ("red", "green", "blue")
print("Tuple:", colors)
print("Access:", colors[0])
# colors[1] = "yellow"   This would raise an error

#  Unpack Tuple
r, g, c = colors
print("Unpacked:", r, g, c)

#  Sets (unordered, no duplicates)
print("====================================")
letters = {"a", "b", "a", "c"}
letters.add("d")
print("Set:", letters)
letters.remove("b")
print("After Remove:", letters)

#  Dictionaries (key-value pairs, ordered from Python 3.7+)
person = {
    "name": "Shan",
    "age": 21,
    "course": "Python"
}
print("Dictionary:", person)
print("Name:", person["name"])
person["age"] = 22               # Update
person["city"] = "Hyderabad"     # Add
del person["course"]             # Delete
print("Updated Dictionary:", person)

#  Nested Dictionary
students = {
    1: {"name": "A", "age": 20},
    2: {"name": "B", "age": 21}
}
print("Nested Dictionary:", students[1]["name"])

