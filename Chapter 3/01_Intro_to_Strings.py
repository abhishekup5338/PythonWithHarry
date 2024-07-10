# The string is immutable in python we have to create new string 
name1 = "Abhi"
name2 = 'Abhi01'
name3 = '''Abhi02'''  #Triple code is used for multiline string

print(name1,name2,name3)

print(len(name1))  #We can find the length of any string


# A string of python can be sliced for a getting a part of the string

nameslice = name2[0:4]  #   Start from index 0 all the way till 4 (excluding 4)
print(nameslice)

character = name1[1] #Give only the 1 index character
print(character)