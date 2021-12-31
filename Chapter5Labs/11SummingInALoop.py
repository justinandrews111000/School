'''
Created on Oct 20, 2021
'''
zork = 0 
print('Before value: {}'.format(zork))

for zorks in [9, 41, 12, 3, 74, 15]:
    zork = zork + zorks
    print('{} {}'.format(zork, zorks))
print('Exit after {}'.format(zork))