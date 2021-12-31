'''
Created on Dec 1, 2021

@author: justi
'''
infile = open(r'C:\Users\justi\Downloads\mbox-short.txt')

for line in infile:
    line = line.rstrip()
    print(line.upper())