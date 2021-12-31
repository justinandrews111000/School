'''
Created on Oct 20, 2021
'''
nums = []
while True:
    num = input('> ')
    
    try:
        if num == 'done':
            print('Done!')
            break
            
        num = int(num)
        nums.append(num)
        print('The amount of numbers entered is: {}'.format(len(nums)))
        print('The sum of the numbers entered is: {}'.format(sum(nums)))
        print('The average of the numbers entered is: {}'.format(sum(nums)/len(nums)))
    
    except:
        print('You must enter numbers.')
        continue