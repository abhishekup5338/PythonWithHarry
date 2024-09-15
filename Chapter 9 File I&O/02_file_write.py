#There are two types of files:
#1- text (.txt, .c etc)
#2- Binary Files(.jpg, .dat, etc)

#Python has a lots of function to reading, updating, and deleting files.


st = "Everyday try to learn something new"

f = open("myfile.txt", "w")

f.write(st)

f.close()