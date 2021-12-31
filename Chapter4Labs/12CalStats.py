import sys

def calstats(num1, num2, num3, num4, num5):
    
    NumMin = min(num1, num2, num3, num4, num5)
    NumMax = max(num1, num2, num3, num4, num5)
    
    NumRange = NumMax - NumMin
    
    Average = (num1 + num2 + num3 + num4 + num5) / 5
    
    print('Min: {}'.format(NumMin))
    print('Max: {}'.format(NumMax))
    print('Range: {}'.format(NumRange))
    print('Average: {}'.format(Average))

try:
    num1 = sys.argv[1]
    num2 = sys.argv[2]
    num3 = sys.argv[3]
    num4 = sys.argv[4]
    num5 = sys.argv[5]
except:
    print('You must input 5 numeric values.')

try:
    num1 = int(num1)
    num2 = int(num2)
    num3 = int(num3)
    num4 = int(num4)
    num5 = int(num5)
    
except: 
    print('Inputs must be numbers, please re-input the values')
    
calstats(num1, num2, num3, num4, num5)


    