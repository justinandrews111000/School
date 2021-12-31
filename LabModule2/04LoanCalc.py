p = int(input('What is the principle: '))
r = float(input('What is the interest rate: '))/100
n = int(input('How many payments are made per year: '))
t = int(input('How many years does the loan last: '))

a = p*(1+r/n)**(n*t)
interest = a - p

print('Interest paid: $'+str(round(interest,1)))