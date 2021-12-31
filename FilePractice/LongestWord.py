'''
Created on Dec 5, 2021

@author: justi
'''
with open(r"C:\Users\justi\My Documents\LiClipse Workspace\IT\Chapter7\studentdata.csv", 'r') as myfile:
    
    longestWord = ''
    longestNum = 0
    for word in myfile:
        length = int(len(word))
        if length > longestNum:
            longestWord = word
            longestNum = int(len(word))
        else:
            continue
    print(longestWord)