import operator
n=input("Input: ").lower()
count = {}
# for letter in n:
    if letter == " ":
        continue
    count[letter]=count.get(letter,0) + 1
count = sorted(count.items(), key=operator.itemgetter(0))

for key,value in count:
    print("{0}:{1}".format(key,value))
