#name1 ="Canh"
#name2 ="Hieu"
#name3 ="Duc Anh"
#name4 ="Nguyen"
#name5 ="Don"

#names = []
#print(names)
#print(type(names))
print("Hi there right now the class have: ")
names = ["Canh","Hieu","Duc Anh"]
print(names, sep=", ") #separator
#Create
while True:
    m= input("Would you like to add somebody else: ")
    names.append(m)

    print("Now the class have")
    print(names)
    break
