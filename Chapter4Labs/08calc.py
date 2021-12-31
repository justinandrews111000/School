from random import randint

def isDivisibleBy6():
    randnum = randint(10, 100)
    
    if randnum % 6 == 0:
        print('{} is divisible by 6'.format(randnum))
    else: 
        print('{} is not divisible by 6'.format(randnum))

isDivisibleBy6()