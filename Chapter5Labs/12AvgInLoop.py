'''
Created on Oct 20, 2021
'''
count = 0
sums = 0
print('Before {} {}'.format(count, sum))
for value in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sums = sums + value
    print(count, sum, value)
print('After', count, sum, sum / count)