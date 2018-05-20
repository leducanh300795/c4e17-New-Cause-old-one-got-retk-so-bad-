print("Hello, my name is Duc Anh and these are my ship sizes")
sheepsize = [5,7,300,90,24,50,75]
print(sheepsize)
m=int(input("Enter the month: "))
a=len(sheepsize)
print()
for j in range(m):
    print("{0} {1}:".format("The Month",j+1))
    for i in range (a):
        sheepsize[i]+=50
    print("{0} {1}".format("One month has passed, now here is my flock:",sheepsize))
    x= max(sheepsize)
    print("{0} {1} {2}".format("Now my biggest sheep size has size", x , "let's hear it"))
    sheepsize[sheepsize.index(x)]=8
    print("After shearing, here is my flock")
    print(sheepsize)
    print()
