'''
Created on Nov 13, 2021
'''
nums = input('Please enter numbers separated by a comma without any spaces: ')
numList = nums.split(',')

Odds = 0
Evens = 0

for i in numList:
    num = int(i)
    if num % 2 == 0:
        Evens = Evens + num
    else:
         Odds = Odds + num
    
print('Odd numbers total: {}, Even numbers total: {}'.format(Odds, Evens))