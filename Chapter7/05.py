'''
Created on Dec 1, 2021

@author: justi
'''
inputdata = open(r"C:\Users\justi\Downloads\mbox-short.txt")

test = open(r"C:\Users\justi\Desktop\test folder\test.txt", 'w')



for line in inputdata:
    strippedLine = line.rstrip()
    strippedLine = strippedLine.strip()
    test.write(strippedLine)