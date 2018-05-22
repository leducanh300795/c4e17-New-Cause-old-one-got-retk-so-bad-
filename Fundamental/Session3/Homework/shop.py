items = ['T-Shirt', 'Sweater']

while True:

    command=input('''Welcome to our shop, what do u want?(C, R, U, D)
(If you want to exit type "done"): ''')
    if command =="done":
        print("Thanks")
        break
    else:
        if command == "R":
            print("Our items: ", end = "")
            print(*items, sep=", ")
        else:
            if command =="C":
                creat=input("Enter the new item: ")
                items.append(creat)
                print(*items, sep=", ")
            else:
                if command =="U":
                    a=int(input("Update position: (Please enter number): "))
                    b=str(input("New item: "))
                    items[a-1]=b
                    print(*items, sep=", ")
                else:
                    if command == "D":
                        c=int(input("Delete position (Please enter number): "))
                        items.remove(items[c-1])
                        print(*items, sep=", ")
                    else:
                        print("Wrong command please try again,: ")
