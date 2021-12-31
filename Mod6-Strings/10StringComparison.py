'''
Created on Nov 8, 2021
'''
word=input('Enter Word: ')

if word == 'banana':
    print('All right, bananas.')

if word < 'banana':
    print('Your word, ' + word + ', is less than a banana.')
elif word > 'banana':
    print('Your word, ' + word + ', is more than a banana.')
else:
    print('All right, bananas.')
