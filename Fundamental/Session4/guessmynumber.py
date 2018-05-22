from random import randint
n = randint(0,100)
i = 0

while i < 9:

    x = int(input("Guess my damn number you scumbag human :): "))
    if x == n:
        print("Bingo, you're correct, well done :)")
        break
    elif x > n:
        print("Too Large, guess again :( ")
        print("{0} ({1} {2})".format("Be careful we will lock you down", (8-i), "times left"))
        print()
        i+= 1
        if 8-i < 0:
            print("You have been suspensed")
    else:
        print("Too Small, like your ding dong :) ")
        print("{0} ({1} {2})".format("Be careful we will lock you down", (8-i), "times left"))
        i+= 1
        if 8-i < 0:
            print("You have been suspensed")
