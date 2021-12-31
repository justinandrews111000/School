'''
Created on Dec 1, 2021

@author: justi
'''
from idlelib.query import SectionName

sectionNum = input('Please input the class section: ')

studata = open(r"C:\Users\justi\Downloads\studentdata.csv")

def findNumGrade(gr):
    if gr == 'A':
        return 4
    elif gr == 'B':
        return 3
    elif gr == 'C':
        return 2

avg = 0 
total = 0
count = 0

for line in studata:
    if ',W,' in line:
        continue 
    else:
        line = line.rstrip()
        
        if line.startswith('Sec'):
            continue
        
        idx = line.find(',')
        secNum = line[:idx]
        line = line[idx + 1:]
        
        if secNum == sectionNum:
            idx = line.find(',')
            profID = line[:idx]
            line = line[idx + 1:]
            
            idx = line.find(',')
            stuID = line[:idx]
            line = line[idx + 1:]
            
            idx = line.find(',')
            courseGrade = line[:idx]
            line = line[idx + 1:]
            
            total += findNumGrade(courseGrade)
            
            count += 1
print('Section {} average is {}'.format(sectionNum, total/count))
            
            
            
            
            
            
            
            
            