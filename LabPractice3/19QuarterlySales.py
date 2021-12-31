import sys

print('Enter the quarterly sales.')

try:
    q1 = int(sys.argv[1])
    q2 = int(sys.argv[2])
    q3= int(sys.argv[3])
    q4 = int(sys.argv[4])
except:
    print('All entries must be numeric values')

print('Quarterly sales: $' + str(q1) + ', $' + str(q2) + ', $' + str(q3) + ', $' + str(q4))

#Adds all quarters to get total
total = q1 + q2 + q3 + q4

#Prints total
print('Total sale: $' + str(total))

#Checks the level of sales
if total < 20000:
    print('Warning sales are under 20K. Too Low, need to improve sales!')
elif total < 50000:
    print('Sales: Low.')
elif 50000 <= total < 150000:
    print('Sales: Medium.')
elif total > 150000:
    print('Sales: High.')