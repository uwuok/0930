weight = float(input('Please input your weight:'))
height = float(input('Please input your height:'))
bmi = weight / ((height / 100) ** 2)
print(f'Your BMI is:{bmi:.2f}')