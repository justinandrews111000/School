'''
Created on Oct 20, 2021
'''
largest = -1

print('Before {}'.format(largest))
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest:
        largest = the_num
    print('{} {}'. format(largest, the_num))
    
print('After {}'. format(largest))