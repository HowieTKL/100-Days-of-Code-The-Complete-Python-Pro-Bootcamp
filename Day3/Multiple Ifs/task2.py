height = int(input("Height (kg): "))
weight = float(input("Weight (m): "))

bmi = height / weight ** 2
print(f"BMI is {round(bmi, 2)}")
if bmi < 18.5:
    print("underweight")
elif bmi >= 25:
    print("overweight")
else:
    print("normal weight")
