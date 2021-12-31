'''
Created on Oct 25, 2021
'''
nums = []


maxV = None
minV = None

while True:
    num = input('> ')
    
    try:
        if num == 'done':
            print('Done!')
            break
            
        num = int(num)
        nums.append(num)
        
        if maxV is None or maxV < num:
            maxV = num
        if minV is None or minV > num:
            minV = num
        
        print('The amount of numbers entered is: {}'.format(len(nums)))
        print('The sum of the numbers entered is: {}'.format(sum(nums)))
        print('The min of the numbers entered is: {}'.format(minV))
        print('The max of the numbers entered is: {}'.format(maxV))
    except:
        print('You must enter numbers.')
        continue