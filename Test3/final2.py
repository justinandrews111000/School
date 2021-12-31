'''
Created on Dec 6, 2021

@author: justi
'''
import sys

user_name = sys.argv[1]
user_item = sys.argv[2]
user_amount = int(sys.argv[3])
user_item_price = float(sys.argv[4])
user_tax = float(sys.argv[5])


def calctotal(name, item, quantity, price, tax):
    
    taxDeci = tax / 100
    taxAmount = taxDeci * (price * quantity) 
    total = taxAmount + (price * quantity)
    if quantity > 1:
        item = item +'s'
        
    
    print('{}, you should pay ${} for your {}'.format(name, round(total, 2), item))
    
calctotal(user_name, user_item, user_amount, user_item_price, user_tax)
    