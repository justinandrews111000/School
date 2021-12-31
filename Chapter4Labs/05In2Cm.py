import sys

def In2Cm(inches):
    centimeter = inches * 2.54
    
    return centimeter

inches = int(sys.argv[1])

print('{} inches = {} centimeters'.format(inches, In2Cm(inches)))

