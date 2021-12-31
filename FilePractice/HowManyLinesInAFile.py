'''
Created on Dec 5, 2021

@author: justi
'''
with open(r"C:\Users\justi\My Documents\LiClipse Workspace\IT\Chapter7\studentdata.csv", 'r') as myfile:
    linecount = 0
    
    for line in myfile:
        linecount += 1
    print(linecount)
        