f = int(input('What is the temp. in Farhrenheit: '))

c = ((f - 32) * 5) / 9

c = round(c, 2)

print('The', f, 'degree Fahrenheit is equal to', c, 'degrees Celsius')