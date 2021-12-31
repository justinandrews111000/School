'''
Created on Oct 25, 2021
'''
stop = -16
total = 0
for number in [6, 5, 3, 7, 4, 4]:
    print(number, end=' ')
    total -= number
    if total < stop:
        print('$')
        break
else:
    print('\ {}'.format(total))
print('done')