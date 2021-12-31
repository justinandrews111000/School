'''
Created on Oct 20, 2021
'''
smallest = -1

print('Before {}'.format(smallest))
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num < smallest:
        smallest = the_num
    print('{} {}'. format(smallest, the_num))
    
print('After {}'. format(smallest))