import random

def attribu(x):
    if x == 1 : 
        return "Rock"
    elif x == 2 :
        return "Paper"
    elif x == 3 : 
        return "Chisel"
    else:
        return "Invalid choice"

User = int(input("Chose between (1 : Rock) , (2 : Paper) , (3 : Chisel) : "))
Guess = random.randint(1, 3)

gg = 0
if Guess == 1 and User == 2 or Guess == 2 and User == 3 or Guess == 3 and User == 1:
    gg += 1
elif Guess == User :
    gg += 2 

Guess = str(attribu(Guess))
attribu(User)


if gg == 2 :
    print(Guess,"vs",Guess)
    print("!DRAW!")
else:
    if gg == 1:
        print("COMPUTER :", Guess)
        print("\n!WINNER!")
    else:
        print("COMPUTER :", Guess)
        print("\n!LOSER!")


