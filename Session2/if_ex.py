yob = int(input("Your year of birth: "))
age = 2018 - yob

if age < 10:
    print("Baby")
if age < 18:
    print("Teenager")
else:
    print("Adult")
