'''
Created on Oct 25, 2021
'''
from random import randint

num = randint(2, 100)

count = 0


for i in range(1, num):
    if num % i == 0:
        count += 1
        
if count <= 2:
    print('{} is prime'.format(num))
else:
    print('{} is not prime'.format(num))
