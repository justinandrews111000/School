import sys

def isDivisible(x, y):
    
    if x % y == 0:
        return "{} is divisible by {}".format(x, y)
    else:
        return "{} is not divisible by {}".format(x, y)
    

x = int(sys.argv[1])
y = int(sys.argv[2])

print(isDivisible(x, y))