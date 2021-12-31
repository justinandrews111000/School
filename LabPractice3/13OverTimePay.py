hours = float(input('How many hours did you work this week: '))
rate = float(input('How much do you get paid per hour: '))

if hours > 40:
    overtime = hours - 40
    overtimepay = (overtime) * (rate * 1.75)
    
    pay = overtimepay + (40 * rate)
else:
    pay = hours * rate
print('Your gross pay is $' + str(pay) + '.')
