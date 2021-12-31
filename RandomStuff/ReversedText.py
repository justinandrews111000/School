'''
Created on Nov 6, 2021
'''
while True:
    user_input = input()
    if user_input == 'done':
        break
    else:
        reversedInput = user_input[::-1]
        print(reversedInput)
        
