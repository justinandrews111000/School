'''
Created on Nov 3, 2021
'''
import sys

inputlen = len(sys.argv) - 1

untaxedTotal = 0
numItems = 0

def taxCalc(untaxedTotal):
    tax = untaxedTotal * .052
    taxedTotal = tax + untaxedTotal
    
    return round(taxedTotal, 2)

for i in range(1, inputlen + 1):
    num = float(sys.argv[i])
    untaxedTotal = untaxedTotal + num
    numItems += 1
    
    if i == inputlen:
        print('Number of items: {}'.format(numItems))
        print('Total of items: ${}'.format(round(untaxedTotal, 2)))
        print('Tax amount: ${}'.format(round(untaxedTotal * .052, 2)))
        print('Total due: ${}'.format(taxCalc(untaxedTotal)))
    