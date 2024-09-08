'''
1 for snake
-1 for water 
0 for gun
'''

computer = -1
youstr = int(input("Enter your Choice : "))
yourDict = {"s" : 1, "w" : -1, "g" : 0}
reverseDict = {1 : "Snake", -1 : "Water", 0 : "Gun"}
you = yourDict[youstr]

print(f"You chose {reverseDict[you]}\n Computer chose {reverseDict[computer]}")

if(computer == you):
    print("It's a Draw")

else:
    if(computer==-1 and you==1):
     print("You win!")

    elif(computer==-1 and you==0):
     print("You Lose!")

    elif(computer==0 and you==1):
     print("You Lose!")

    elif(computer==0 and you==-1):
     print("You win!")
 
    elif(computer==1 and you==0):
     print("You win!")

    elif(computer==1 and you==-1):
     print("You lose_--!")

    else:
     print("Something went Wrong!")