'''
Created on Oct 25, 2021
'''
from random import randint
x = randint(1, 100)
y = randint(1, 100)

if x > y:
    maxV = x
    minV = y
else:
    maxV = y
    minV = x

print('Min: {}'.format(minV))
print('Max: {}'.format(maxV))

while minV <= maxV:
    print(minV)
    minV += 1

