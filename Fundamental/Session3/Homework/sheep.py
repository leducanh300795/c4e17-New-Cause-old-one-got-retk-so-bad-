print("Hello, my name is Duc Anh and these are my ship sizes")
sheepsize = [5,7,300,90,24,50,75]
print(sheepsize)

print("Now my biggest sheep size has size", max(sheepsize) , end=" ")
print("let's hear it")

sheepsize[sheepsize.index(max(sheepsize))]=8
print("After shearing, here is my flock")
print(sheepsize)

for i in range(len(sheepsize)):
    sheepsize[i] += 50
print("One month has passed, now here is my flock")
print(sheepsize)
