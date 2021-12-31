hours = int(input('How many hours did you work: '))
rate = float(input('How much do you get paid per hour: '))

pay = hours * rate
pay = round(pay, 2)

print('The gross pay for', hours, 'hours with $' + str(rate) + ' per hour is $' + str(pay) + '.')