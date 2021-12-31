'''
Created on Nov 13, 2021
'''
student_input = input('Enter Student Grades: ')

stuList = student_input.split()

total = 0
avg = 0

for i in stuList:
    temp = i.split(':')
    name = temp[0]
    temp = temp[1].split(',')
    if total != 0:
        total = 0 
    for i in temp:
        num = i
        total = total + int(num)
    avg = int(total) / len(temp) 
    print('{}\'s average: {}'.format(name, avg))     