import sys


def calcInterest(Principle, Rate, PaymentsPerYear, LengthInYears):
    
    accrued = Principle * (1 + Rate/PaymentsPerYear) ** (PaymentsPerYear * LengthInYears)
    interest = round(accrued - Principle, 1)
    
    print('Interest Paid: ${}'.format(interest))
    
p = float(sys.argv[1])
r = float(sys.argv[2])/100
n = int(sys.argv[3])
t = float(sys.argv[4])

calcInterest(p, r, n, t)