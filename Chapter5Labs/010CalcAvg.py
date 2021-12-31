'''
Created on Nov 1, 2021
'''
import sys


inputlen = len(sys.argv)


def calcavg(user_input):
    count = 0
    total = 0
    for i in range(1, inputlen):
        num = float(sys.argv[i])
        
        count += 1
        
        total = num + total
        
        avg = total / count
    
    return avg

print('The average is {}'.format(calcavg(sys.argv)))
        
    