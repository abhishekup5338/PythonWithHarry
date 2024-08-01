#Write a program to greet all the person name store in list 'l' and which start with 'S'.

l = ["Abhi", "Sam", "anup", "Shiv", "Soham", "harry"] #This is list

for name in l: #logic
    if(name.startswith("S")): 
        print(f"Hello {name}")