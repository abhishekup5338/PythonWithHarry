import random

def game():
    print("Your are playing a game...")
    score = random.randint(1, 65)
    #Fetch the Hiscore
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore!=""):
            hiscore=int(hiscore)
        else:
            hiscore = 0
    print(f"Your score : {score}")
    if(score>hiscore):
        #write this to the file
        with open("hiscore.txt", "w") as f:
            f.write(str(score))

    return score

game()