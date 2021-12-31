name = input('What is your name: ')
h = int(input('What is your height in inches: '))
w = int(input('what is your weight in pounds: '))

bmi = (w/(h*h))*703

print(name+'\'s BMI is', round(bmi,2))