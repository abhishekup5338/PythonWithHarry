import random

'''
1 for snake
-1 for water 
0 for gun
'''

computer = random.choice([-1, 0, 1])
youstr = input("Enter your Choice : ")
yourDict = {"s" : 1, "w" : -1, "g" : 0}
reverseDict = {1 : "Snake", -1 : "Water", 0 : "Gun"}
you = yourDict[youstr]

#As of now we have 2 number (variable) Youstr and Computer
#The below logic is return on the basis of computer - you

print(f"You chose {reverseDict[you]}\n Computer chose {reverseDict[computer]}")

if(computer == you):
    print("It's a Draw")

else:
    if((computer - you) == -1 or (computer - you) == 2):
        print("You Lose!")
    else:
        print("You Win!")

# else:
#     if(computer==-1 and you==1):
#      print("You win!")

#     elif(computer==-1 and you==0):
#      print("You Lose!")

#     elif(computer==0 and you==1):
#      print("You Lose!")

#     elif(computer==0 and you==-1):
#      print("You win!")
 
#     elif(computer==1 and you==0):
#      print("You win!")

#     elif(computer==1 and you==-1):
#      print("You lose_--!")

#     else:
#      print("Something went Wrong!")