from random import choice
a = "champion"
b = list(a)
for i in range(len(a)):
    c = choice(b)
    print(c, end = " ")
    b.remove(c)
print()

run = True
while run:
    e = input("Your Answer: ")
    if e == a:
        print("Hura")
        run = False
    else:
        print("Again :(!")
