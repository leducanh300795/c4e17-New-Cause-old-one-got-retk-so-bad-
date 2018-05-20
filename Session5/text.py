
numbers = [7,-10,2,8,11,200]
n = int(input("Enter a number? "))
a=numbers.count(n)
if a!=0:
    print("This number existed in the list")
else:
    print("This number didn't existed in the list ")
