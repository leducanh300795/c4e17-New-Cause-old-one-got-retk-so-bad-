person={
    "name": "Quan",
    "age": 22,
    "gender":"undefined"
}
# if "name" in person: # tuong duong
if "name" in person.keys():
    print("Yeahhh")
print(person.keys())
print(person.values())

for keys,values in person.items():
    print(keys, ":", values)
