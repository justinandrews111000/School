import math
import sys
def calc(x, y, z):
    
    total = (math.sqrt(math.pow(x, 1))) + (math.sqrt(math.pow(y, 2))) + (math.sqrt(math.pow(z, 3)))
    return total

x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

print("{:.2f}".format(calc(x, y, z)))