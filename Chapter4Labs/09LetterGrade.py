import sys

def getLetter(average):
    if 0 <= average <= 1: 
        if average >= 0.9:
            letter = 'A'
        elif average >= 0.8:
            letter = 'B'
        elif average >= 0.7:
            letter = 'C'
        elif average >= 0.6:
            letter = 'D'
        elif average < 0.6:
            letter = 'F'
    
    return letter

def calcavg(num1, num2, num3, num4, num5):
    average = ((num1 + num2 + num3 + num4 + num5) / 5) / 100
    
    return average

def printresults(average, letter):
    print('Average: {}'.format(average))
    print('Letter Grade: {}'.format(letter))

try:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    num3 = int(sys.argv[3])
    num4 = int(sys.argv[4])
    num5 = int(sys.argv[5])

    printresults(calcavg(num1, num2, num3, num4, num5) * 100, getLetter(calcavg(num1, num2, num3, num4, num5)))

except:
    print('You must input 5 numeric values for the program to work.')