
a = int(input("Enter your age : "))

#if elif else ladder

if(a>=18):
    print("You can vote")
elif(a<0):
    print("You are entering a invalid negative age")
elif(a==0):
    print("You are entering 0 is not a invalid age")
else:
    print("You cannot vote")

print(a)
print("Ens of program")