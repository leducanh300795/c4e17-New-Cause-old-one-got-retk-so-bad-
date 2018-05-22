inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
n=int(input("Input: "))

if n == 1:
    inventory["pocket"] = ["seashell","strage berry","lint"]
elif n == 2:
    inventory["backpack"].remove("dagger")
elif n == 3:
    inventory["gold"] +=50
for key, value in inventory.items():
    print(key, ":", value)
    print()
