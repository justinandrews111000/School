'''
Created on Dec 5, 2021

@author: justi
'''
numlines = int(input('How many of the last lines would you like to read: '))

with open(r"C:\Users\justi\My Documents\LiClipse Workspace\IT\Chapter7\studentdata.csv", 'r') as myfile:
    
    filelength = 0
    for lines in myfile:
        filelength += 1
        
    x = 0
    
    startnum = filelength - numlines

with open(r"C:\Users\justi\My Documents\LiClipse Workspace\IT\Chapter7\studentdata.csv", 'r') as myfile:
    for line in myfile:
        if x >= (startnum):
            x += 1
            print(line)
        elif x < startnum:
            x += 1
            
            
            