'''
Created on Oct 27, 2021
'''
import sys


inputlen = len(sys.argv)

OddTotal = 0
EvenTotal = 0

for i in range(1, inputlen):
    num = int(sys.argv[i])
    
    if num % 2 == 0:
        EvenTotal += num
    else:
        OddTotal += num
print('Odd sum: {}'.format(OddTotal))
print('Even sum: {}'.format(EvenTotal))
            
    
