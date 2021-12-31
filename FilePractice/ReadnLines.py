'''
Created on Dec 5, 2021

@author: justi
'''
myfile = open(r"C:\Users\justi\My Documents\LiClipse Workspace\IT\Chapter7\studentdata.csv")


numOfLines = int(input('How many lines from your file do you want to read: '))

x = 0

for line in myfile:
    if x != numOfLines:
        print(line)
        x +=1
        continue
    else:
        break
    