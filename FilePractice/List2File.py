'''
Created on Dec 5, 2021

@author: justi
'''
with open(r"C:\Users\justi\My Documents\LiClipse Workspace\IT\Chapter7\studentdata.csv", 'r') as orgfile:
    with open(r"C:\Users\justi\My Documents\LiClipse Workspace\IT\Chapter7\test.txt", 'w') as copyfile:
        
        
        wordList = []
        for line in orgfile:
            wordList.append(line)
            
        for i in wordList:
            copyfile.write(i)
            
    