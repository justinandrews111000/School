import sys
import math

def AreaSquare(Length):
    SquareArea = Length * Length 
    return round(SquareArea, 2)

def AreaCircle(Radius):
    CircleArea = float(math.pi * (Radius ** 2))
    return round(CircleArea, 2)

def shapes(CircleOrSquare, RadiusOrLength):
    if CircleOrSquare == 'Square':
        print('The squares area is {}'.format(AreaSquare(RadiusOrLength)))
    elif CircleOrSquare == 'Circle':
        print('The circles area is {}'.format(AreaCircle(RadiusOrLength))) 

shape = sys.argv[1]
length = float(sys.argv[2])

shapes(shape, length)