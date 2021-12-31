'''
Created on Nov 3, 2021
'''
import sys

fallCred = float(sys.argv[1])
springCred = float(sys.argv[2])
summerCred = float(sys.argv[3])

def ave_credit_hours(fallCred, springCred, summerCred):
    total = fallCred + springCred + summerCred
    avg = 'The average credits per semester is {}'.format(total / 3)
    
    return avg

print(ave_credit_hours(fallCred, springCred, summerCred))

  