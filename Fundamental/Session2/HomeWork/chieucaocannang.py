m = float(input("Please input your weight: "))
h = float(input("Please input your height(cm): "))
h = h/100
bmi = m/(h**2)
if bmi < 16:
    print("Severely underweight")
elif bmi >= 16 and bmi <18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi < 25:
    print("Normal")
elif bmi >= 25 and bmi < 30:
    print("Overweight")
else:
    print("Obese")
