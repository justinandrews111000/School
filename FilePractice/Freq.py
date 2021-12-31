'''
Created on Dec 5, 2021

@author: justi
'''
with open(r"C:\Users\justi\My Documents\LiClipse Workspace\IT\Chapter7\studentdata.csv", 'r') as myfile:
    
    wordToCount = input('What word would you like to look for: ')
    freq = 0
    
    for line in myfile:
        if wordToCount in line:
            freq += 1
        else:
            continue
print('{} appears {} times.'.format(wordToCount, freq))
            