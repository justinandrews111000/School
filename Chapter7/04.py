'''
Created on Dec 1, 2021

@author: justi
'''
import sys

myFile=open(
r"C:\Users\justi\Downloads\studentdata.csv")

def findnumericgrade(gr):
    if gr=='A':
        return '4.0'
    elif gr=='B':
        return '3.0'
    elif gr=='C':
        return '2.0'

def loaddata(myfile):
    output=open(r"C:\Users\justi\Desktop\Output\output.txt",'w')
    errorf=open(r"C:\Users\justi\Desktop\Error\error.txt",'w')
    cou=0
    for lines in myfile:
        if ',W,' in lines:
            errorf.write(lines)
        else:
            
            
            lines=lines.rstrip()
            if lines.startswith('Sec'):
                continue
            elif lines[13]==',':
                index1=lines.find(',',15)
                name=lines[14:index1]
            elif lines[14]==',':
                index1=lines.find(',',15)
                name=lines[15:index1]
            
            class1=lines[index1+1:]
            
            index2=lines.find(',')
            sec=lines[:index2]
            
            index3=lines.find(',',6)
            num1=lines[6:index3]
            
            index4=lines.find(',',9)
            index5=lines.find(',',13)
            grade=lines[index4+1:index5]
            
            gpa=findnumericgrade(grade)
            strin=(name+': '+class1+' '+sec+' '+num1+' '+grade+' '+gpa)
            output.write(strin)
            output.write('\n')
            
            cou=cou+1
        
    print('Lines:',cou)
        
    for lines in myfile:
        if ',W,' in lines:
            errorf.write(lines)
        


loaddata(myFile)

