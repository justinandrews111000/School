'''
Created on Dec 1, 2021

@author: justi
'''

stuName = input('Please enter the student\'s name: ')
myFile = open(r"C:\Users\justi\Downloads\studentdata.csv")

def findnumericgrade(gr):
    if gr=='A':
        return 4.0
    elif gr=='B':
        return 3.0
    elif gr=='C':
        return 2.0

def loaddata(myfile, stuName):
    ITcou=0
    CScou = 0
    CStotal = 0
    ITtotal = 0
    for lines in myfile:
        
        if stuName in lines:
            idx = lines.find(stuName)
            
            grade = lines[idx - 2: idx - 1]
            classSym = lines[idx + len(stuName) + 1:]
            
            stuClasses = '{}    {}'.format(grade, classSym)
            print(stuClasses)
            
            if 'IT' in classSym:
                ITtotal += findnumericgrade(grade)
                ITcou += 1
            else:
                CStotal += findnumericgrade(grade)
                CScou += 1
    ITavg = ITtotal / ITcou
    CSavg = CStotal /CScou 
    print('{}\'s IT courses average is: {}, and CS courses average: {}'.format(stuName, round(ITavg, 2), round(CSavg, 2)))   
            


loaddata(myFile, stuName)