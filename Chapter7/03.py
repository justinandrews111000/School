'''
Created on Dec 1, 2021

@author: justi
'''

import sys
myfile = open(r"C:\Users\justi\Downloads\studentdata.csv")

def loaddata(myfile):
    errorf = open(r"C:\Users\justi\Desktop\Errorbah\Error.txt", 'w')
    
    cou = 0
    for lines in myfile:
        if ',W,' in lines:
            errorf.write(lines)
loaddata(myfile)
