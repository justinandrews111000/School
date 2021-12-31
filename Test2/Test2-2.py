'''
Created on Nov 3, 2021
'''
import sys

inputlen = len(sys.argv) - 1
total = 0

for i in range(1, inputlen):
    num = float(sys.argv[i])
        
    total = total + num
    
    if i == inputlen:
        semesters = i
        avg = total / semesters

        print('Total semesters is {}'.format(semesters))
        print('Average credits per semester is {}'.format(avg))