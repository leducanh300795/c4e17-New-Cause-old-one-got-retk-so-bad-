# person = ["Quan", 40, "Single", "Hanoi", 2, 11]
# print(person)
# person={
#     "name":"Quan"
# }
#
# print(person)

person = {
    "name": "Quan",
    "age": 40,
}

#Update
person["age"] = 22
print(person)

#Creat
person["home"] = "Hanoi"
print(person)

#Delete
del person["age"]
print(person)

print(*person.keys())
print(*person.values())

for value in person.values():
    print(value)

for key, value in person.items():
    print(key, ":", value)

#print(person)
# print(person["age"])
# person["age"] = 22
# print(person)
#
# if "home" in person:
#     print(person["home"])
# else:
#     print("'home' is not in person")
