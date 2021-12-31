'''
Created on Dec 1, 2021

@author: justi
'''
myfile = open(r"C:\Users\justi\Downloads\test.txt")

maxWord = 0
longWord = None
total = myfile.read()

idx = total.find(' ')

while idx != -1:
    word = total[:idx]
    if (len(word) > maxWord):
        maxWord = len(word)
        longWord = word
        
    total = total[idx + 1:]
    idx = total.find(' ')
        
word = total

if (len(word) > maxWord):
    maxWord = len(word)
    longWord = word
    
print('The longest word is {} and it has {} characters'.format(longWord, maxWord))