numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
for num in numbers:
    print("\t ", num)
x=int(input("Enter a number: "))
if numbers.count(x) != 0:
    print("{0} {1}".format(x,"is in the list"))
else:
    print("{0} {1}".format(x,"isn't in the list"))
