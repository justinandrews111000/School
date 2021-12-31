num1 = int(input('Enter your first number (int): '))
num2 = float(input('Enter your second number (float): '))

print('Number 1 is', num1)
print('NUmber 2 is', num2)

outputOne = (num1 // 2)
print(num1, '// 2 = ' + str(outputOne) + ',', type(outputOne))

outputTwo = (num1 / num2)
print(num1, '/ ' + str(num2) + ' = ' + str(outputTwo) + ' ,', type(outputTwo))

outputThree = (num1 * num2)
print(num1, '* ' + str(num2) + ' = ' + str(outputThree) + ' ,', type(outputThree))

outputFour = (3 ** num2)
print('3 ** ' + str(num2) + ' = ' + str(outputFour) + ' ,', type(outputFour))