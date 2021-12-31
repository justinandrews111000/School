'''
Created on Oct 25, 2021
'''
while True:
    num = input('> ')
    
    try:
        if num == 'done':
            print('Done!')
            break
            
        num = int(num)
        
        if num % 2 != 0:
            print(num)
        
    except:
        print('You must enter numbers.')
        continue