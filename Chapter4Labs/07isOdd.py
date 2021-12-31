import sys

def OddOrNot(number):
    OddOrEven = number % 2
    
    if OddOrEven == 0:
        print(number, 'is not an odd number')
    elif OddOrEven == 1:
        print(number, 'is an odd number')

number = int(sys.argv[1])

OddOrNot(number)