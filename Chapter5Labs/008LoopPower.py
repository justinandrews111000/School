'''
Created on Oct 27, 2021
'''
base = int(input('Please input the base: '))
power = int(input('Please input the power: '))
pow = 2
absBase = base


while pow <= power:
    absBase = absBase * base
    pow += 1

print(base, 'Power', str(power) + ':', absBase)