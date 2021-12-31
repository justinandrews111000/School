'''
Created on Dec 5, 2021

@author: justi
'''
with open(r"C:\Users\justi\My Documents\LiClipse Workspace\IT\Chapter7\studentdata.csv", 'r') as myfile:
    
    lineVar = ''
    
    for line in myfile:
        lineVar = lineVar + line
        
    print(lineVar)