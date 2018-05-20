#How do we convert  a string to uppercase or lowercase?
a="Hello World"
b=a.upper()
print(b)
c=a.lower()
print(c)
#How do we get length of a string?
d=len(a)
print(d)
#How do we print a string, one character per line?
for i in range(len(a)):
    print(a[i])

#How do we compare two strings?
#Other comparison operations are useful for putting words in lexicographical order:
word=str(input("Enter your word: "))
if word < "banana":
    print("Your word, " + word + ", comes before banana.")
elif word > "banana":
    print("Your word, " + word + ", comes after banana.")
else:
    print("Yes, we have no bananas!")
