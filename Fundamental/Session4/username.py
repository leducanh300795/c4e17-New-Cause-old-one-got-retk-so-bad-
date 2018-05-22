n=0
while n < 4:
    username = input("Username? ")
    password = input("Password? ")
    if username != 'c4e':
        print("No such user")
        print("{0} ({1} {2})".format("Please try again, be careful we will lock you down", (3-n), "times left"))
        n+= 1
        if 3-n < 0:
            print("You have been suspensed")
    else:
        if password != 'codethechange':
            print("Wrong password")
            print("{0} ({1} {2})".format("Please try again, be careful we will lock you down", (3-n), "times left"))
            n+= 1
            if 3-n < 0:
                print("You have been suspensed")
        else:
            print("Welcome!!!")
            break
