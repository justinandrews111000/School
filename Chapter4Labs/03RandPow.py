import math
from random import randint

def powRand():
    x = randint(1, 10)
    y = randint(1, 10)
    
    
    print('{} power {} is {}'.format(x, y, math.pow(x, y)))
    
powRand()



    