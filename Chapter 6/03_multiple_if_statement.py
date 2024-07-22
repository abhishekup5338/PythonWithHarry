
a = int(input("Enter your age : "))
#if statement no : 1
if(a>=45):
    print("Old age")
#End of if statement no : 1

#if statement no : 2
if(a>=18):
    print("You can vote")
elif(a<0):
    print("You are entering a invalid negative age")

else:
    print("You cannot vote")

#End of if statement no : 2

print(a)
print("Ens of program")