nums = [3, 4, -99, 78, 4, -99]
x = int(input("Enter a integer: " ))
#must not use count() or in or index()
found = False

for num in nums:
    if num == x:
        found = True
        break

if found:
    print("Found!!!")
else:
    print("Not Found")
