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
# print(*names, sep=", ") #separator
#Create
# print(len(names)) # len  = length

# print(names[-3])
# for i in range(len(names)): #for i
#     print(names[i])

# for i in range(len(names)):
#     print(i+1,names[i])
no = 1
for n in names:
        # print(no,".",n, sep="")
        # string format
        message = "{0}. {1}".format(no, n)
        print(message)
        no = no +1 # no += 1
