'''
Created on Oct 20, 2021
'''
zork = 0

print('Before {}'.format(zork))
for zorks in [9, 41, 12, 3, 74, 15]:
    zork = zork + 1
    print('{} {}'.format(zork, zorks))
print('After {}'.format(zork))