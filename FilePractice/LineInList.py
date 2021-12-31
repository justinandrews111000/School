'''
Created on Dec 5, 2021

@author: justi
'''
with open(r"C:\Users\justi\My Documents\LiClipse Workspace\IT\Chapter7\studentdata.csv", 'r') as myfile:
    
    lineList = []
    
    for line in myfile:
        lineList.append(line)
        
    print(lineList)
        