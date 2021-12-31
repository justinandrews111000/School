'''
Created on Nov 13, 2021
'''
word = input('Please enter a word: ')

colonloc = word.find(':')
wordEnd = len(word)

print(word[colonloc + 1:wordEnd])
