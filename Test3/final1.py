'''
Created on Dec 6, 2021

@author: justi
'''
import sys

user_input = input('Enter a word: ')

vowels = ['a','e','i','o','u']
Vcount = 0

for i in user_input:
    if Vcount == 2:
        break
    
    elif i in vowels:
        Vcount += 1
        print(i)
        continue
    else:
        print(i)
        
    