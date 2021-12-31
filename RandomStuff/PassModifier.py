'''
Created on Oct 27, 2021
'''

user_pass = input('Enter Your password to totally make it stronger and not just steal it I promise.')

def splitpass(user_pass):
    for i in user_pass:
        if i == 'i':
            i = '1'
            print(i, end = '')
        elif i == 'a':
            i = '@'
            print(i, end = '')
        elif i == 'm':
            i = 'M'
            print(i, end = '')
        elif i == 'B':
            i = '8'
            print(i, end = '')
        elif i == 's':
            i = '$'
            print(i, end = '')
        else:
            print(i, end = '')
            continue
    print('!')
splitpass(user_pass)
        



