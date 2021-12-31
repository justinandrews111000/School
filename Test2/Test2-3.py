'''
Created on Nov 3, 2021
'''
import sys

inputlen = len(sys.argv) - 1
x = 0
total = 0
grades = 0

while x != inputlen:
    x += 1
    grades += 1
    num = float(sys.argv[x])
    
    total = num + total
    
print('Total number of grades is {}'.format(grades))
print('GPA is {}'.format(float(total / grades)))
    
