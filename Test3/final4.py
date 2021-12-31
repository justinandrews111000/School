'''
Created on Dec 6, 2021

@author: justi
'''
import sys

user_Lname = sys.argv[1]
user_Fname = sys.argv[2]

user_C1 = sys.argv[3]
user_C2 = sys.argv[4]
user_C3 = sys.argv[5]
user_C4 = sys.argv[6]

def findnumericgrade(gr):
    if gr=='A':
        return 4.0
    elif gr=='B':
        return 3.0
    elif gr=='C':
        return 2.0
    
grades = []

def myaverage(Lastname, Firstname, Class1, Class2, Class3, Class4):
    
    grades.append(Class1) 
    grades.append(Class2)
    grades.append(Class3)
    grades.append(Class4)
    
    if 'W' in grades:
        print('{}, you should complete 4 courses to get your GPA calculated.'.format(user_Fname))
        
    else:
        GPA = (findnumericgrade(Class1) + findnumericgrade(Class2) + findnumericgrade(Class3) + findnumericgrade(Class4)) / 4
        print('{}, your semester GPA is {}.'.format(user_Lname, round(GPA, 2)))

myaverage(user_Lname, user_Fname, user_C1, user_C2, user_C3, user_C4) 
