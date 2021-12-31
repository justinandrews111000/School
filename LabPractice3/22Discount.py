try:
    p1 = int(input('How many items did you purchase: '))
except:
    print('Please enter a numeric value!')
total = 100 * p1

print('Your total is: $', total)

if total >= 800:
    discount = total * 0.1
    cost  = total - discount
    print('Your discount is: $' + str(discount) + ' and the total cost after the discount is $' + str(cost) + '.')
else:
    print('No discount')