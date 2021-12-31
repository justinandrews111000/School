#Commands for console
import sys

d1 = float(sys.argv[1])
d2 = float(sys.argv[2])
d3 = float(sys.argv[3])
d4 = float(sys.argv[4])
d5 = float(sys.argv[5])

age = float(sys.argv[6])

avg = (d1 + d2 + d3 + d4 + d5) / 5

#Under 18 y/0
if age < 18:
    print('This program is for adults(18+) only!')

#Over 18 and under 65
elif (18 <= age < 65) and (avg < 7):
    print('Average:',avg)
    print('Sleep type: Too little')

elif (18 <= age < 65) and (7 <= avg <= 9):
    print('Average:',avg)
    print('Sleep type: Normal')

elif (18 <= age < 65) and (avg > 9):
    print('Average:',avg)
    print('Sleep type: Too much')

#Over 65 y/o
elif (age >= 65 and avg < 7):
    print('Average:',avg)
    print('Sleep type: Too little')
    
elif (age >= 65) and (7 <= avg <= 8):
    print('Average:',avg)
    print('Sleep type: Normal')

elif (age >= 65 and avg > 8):
    print('Average:',avg)
    print('Sleep type: Too much')