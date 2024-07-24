#Write a program to greet all the person name store in list 'l' and which start with 'S'.

l = ["Abhi", "Sam", "anup", "Shiv", "Soham", "harry"]

for name in l:
    if(name.startswith("S")):
        print(f"Hello {name}")