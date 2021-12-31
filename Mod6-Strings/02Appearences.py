'''
Created on Nov 10, 2021
'''
word = input('Please enter a word: ')
letter = input('Enter a letter to see how many times it appears in the word entered.')

occurences = 0

for i in word:
    if i == letter:
        occurences += 1
    else:
        continue 
print('There are {} {}\'s in {}'.format(occurences, letter, word))