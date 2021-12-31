'''
Created on Oct 20, 2021
'''
smallest = None
print('Before')
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None: #is compares the value, while == compares the type and value
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print('After {}'.format(smallest))