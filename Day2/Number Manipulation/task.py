height = int(input("Height (kg): "))
weight = float(input("Weight (m): "))

bmi = height / weight ** 2
print(f"BMI is {round(bmi, 2)}")
