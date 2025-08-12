#string methods--
#1.len()-->to find lenght
str1='shanmukha10kcoders'
print(len(str1))

#2.upper()-->convert uppercase
print('upper()',str1.upper())

#3.lower() -->convert lowercase
print('lower()',str1.lower())

#4.strip()-->it removes white spaces from both ends
str1='   shanmu k h a      a  '
print(str1.strip())

#5.lstrip()-->it removes white spaces only from left end
str1='   shanmu k h a      a  '
print(str1.lstrip())

#6.rstrip()-->it removes white spaces only form right side
str1='   shanmu k h a      a     '
print(str1.rstrip())

str='******shannu hi *****'
print(str.strip("*"))
print(str.lstrip('*'))
print(str.rstrip('*'))

#7.replace()-->it replaces all theoccurences of a word with word specifird it
str3='hello hi naveen,Good morning naveen,how are you naveen'
print(str3.replace("naveen","shannu"))

#8.join():-it combines two or mote strings
str3='shanni','hii','navven','hi'
print(''.join(str3))