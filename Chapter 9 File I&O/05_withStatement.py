
f = open("myfile.txt")

print(f.read())
f.close()

#This same can be return using with statement like this :

with open("myfile.txt") as f:
    print(f.read())

#You don't have to expilicitly close the file