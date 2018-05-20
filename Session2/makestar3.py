#n=int(input("How many star you want hang doc:  "))
#m=int(input("How many star you want hang doc:  "))
#for i in range (n):
    #print ("*" , end= "")
#print(end='\n')

n=int(input("How many star you want in column:  "))
m=int(input("How many star you want in row:  "))
for i in range(n):
    for j in range (m):
        if i >=j:
            print("*", end="")
        else:
            print("", end="")
    print()
