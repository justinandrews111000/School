'''
Created on Nov 13, 2021
'''
word = input('Please enter a word: ')
vowels = ['a', 'e', 'i', 'o', 'u', 'y']

vcount = 0
ccount = 0

for char in word:
    if char in vowels:
        vcount += 1
    else:
        ccount += 1
print(word)
print('Vowels:{}, Consonants:{}'.format(vcount, ccount))