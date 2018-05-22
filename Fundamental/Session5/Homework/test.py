# import operator
# n=input("Input: ").lower()
# count = {}
# for letter in n:
#     if letter == " ":
#         continue
#     count[letter]=count.get(letter,0) + 1
# count = sorted(count.items(), key=operator.itemgetter(0))
#
count = {"a":4,"b":2}
count["a"]=count.get("a",1) + 1
print(count)
