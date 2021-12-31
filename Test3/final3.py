'''
Created on Dec 6, 2021

@author: justi
'''
import sys

try:
    user_name = sys.argv[1]
    user_quantity = int(sys.argv[2])
    item_price = float(sys.argv[3])

    total = user_quantity * item_price

    if user_quantity < 10:
        print('It\'s a wholesale company, and quantity should be at least 10')
    elif user_quantity > 20:
        print('Quantity is limited to no more than 20')
    elif 10 <= user_quantity <= 20:
        print('Thank you for your oder {}. Your oder total is ${}'.format(user_name, round(total, 2)))
    
except:
    print('Invalid data entered')
        
    
