nums= [1, 5, -9, 81, 55, 123, -135, 5]
x = int(input("Enter a interger: "))

#in
if x in nums: # in => list, dictionary
    print("Found in list")
else:
    print("Not found in list")

c=nums.count(x)
print(c)
