time = int(input('Enter military time (0-2400): '))

if (0 <= time <= 500):
    print('Good night!')
elif (500 <= time <= 1200):
    print('Good morning!')
elif (1200 <= time <= 1600):
    print('Good afternoon!')
elif (1600 <= time <= 1900):
    print('Good evening!')
elif (1900 <= time <= 2400):
    print('Good night!')