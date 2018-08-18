#TUPLES
#answer1:to reverse a tuple:
tuple=('q','a','n','s','i')
reverse=tuple[::-1]
print("reversed tuple is",reverse)

#answer2:
tuple=(1,21,4,6,19)
max_value=max(tuple)
min_value=min(tuple)
print("Maximum value is",max_value)
print("Minimum value is",min_value)




#STRINGS
#answer1:
import string
str=input("enter a string\n")
print(str.upper())

#answer2:
str=input("enter a string\n")
print(str.isdigit()) #to check if it contains all numeric charcaters or not

#answer3:
str='Hello World'
new_str= str.replace("World","Arshia")
print(new_str)
