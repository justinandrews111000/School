'''
Created on Nov 1, 2021
'''
import sys

inputlen = len(sys.argv)

def calstats(user_input):
    vmin = None
    vmax = None
    total = 0
    cont = 0
    for i in range(1, inputlen):
        num = float(sys.argv[i])
        cont += 1
        
        if vmin == None:
            vmin = num
        else:
            if num < vmin:
                vmin = num
        
        if vmax == None:
            vmax = num
        else:
            if num > vmax:
                vmax = num
        
        total = num + total
    print('Min: {}'.format(vmin))
    print('Max: {}'.format(vmax))
    print('Range: {}'.format(vmax - vmin))
    print('Average: {}'.format(round(total/cont,2)))

calstats(sys.argv)
        