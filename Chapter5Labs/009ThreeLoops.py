'''
Created on Oct 27, 2021
'''




num1 = int(input())
num2 = int(input())
num3 = int(input())

def loopeven(num1):
    print('First Loop: ')
    for i in range(1, num1 + 1):
        if i % 2 == 0:
            print(i)
    
def loopsum(num2):
    print('Second Loop: ')
    total = 0
    for i in range(1, num2 + 1):
        total = total + i
    print(total)
    
def loopthree(num3):
    print('Third Loop: ')
    cont = 0
    for i in range(1, num3 + 1):
        if num3 % 3 == 0:
            print(i, end = ' ')
            cont += 1
            if cont % 3 == 0:
                print('')
        else:
            print('This one won\'t work')    
                

loopeven(num1)
loopsum(num2)
loopthree(num3)