import getpass

while True:
    print("Welcome to superuser gateaway")
    username= input("Please input your username :")
    password= getpass.getpass("Enter password: ")
    if username != "C4E":
        print("We don't have this username, please input again")
    else:
        if password != "codethechange":
            print("We don't have this username, please input again")
        else:
            print("Welcome")
            break
