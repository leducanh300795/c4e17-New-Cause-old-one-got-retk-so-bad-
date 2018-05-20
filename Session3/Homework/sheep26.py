print("Hello, my name is Duc Anh and these are my ship sizes")
sheepsize = [5,7,300,90,24,50,75]
print(sheepsize)
n = int(input("Enter the number of months: "))
maxsize = max(sheepsize)
print("Now my biggest sheep has size ", maxsize, " let's shear it")
a = sheepsize.index(maxsize)
sheepsize[a] = 8
print("After shearing, here is my flock")
print(sheepsize)
for i in range(n):
    print("{0} {1}:".format("MONTH",i+1))
    for j in range(len(sheepsize)):
        sheepsize[j] += 50
    print("One month has passed, now here is my flock" + "\n", sheepsize)
    if i<n-1:
        maxsize = max(sheepsize)
        print("{0} {1} {2}".format("Now my biggest sheep has size", maxsize, "let's shear it"))
        a = sheepsize.index(maxsize)
        sheepsize[a] = 8
        print("After shearing, here is my flock"+"\n",sheepsize)
    print()
total = sum(sheepsize)
price  = total * 2
print("{0}{1}{2}".format("My flock has size in total: ", total, "\n"))
print("{0}{1}{2}{3}{4}{5}{6}".format("I would get ",total, " * ","2$ ", "= ", price,"$"))
