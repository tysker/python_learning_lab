# If else statements

height = 193
age = 19

if height >= 120:
    print("He is large")
    if age >= 30:
        print("He is getting older!")
    elif age < 20:
        print("The person is still a teenager!")
    else:
        print("He is still young!")
else:
    print("He is small")

# BMI Calculations

weight = 85
height = 1.85

bmi = weight / (height**2)

if bmi < 18.5:
    print("underweight")
elif 18.5 <= bmi < 25:
    print("normal weight")
else:
    print("overweight")
