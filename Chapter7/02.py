'''
Created on Dec 1, 2021

@author: justi
'''
infile = open(r"C:\Users\justi\Downloads\mbox-short.txt")

tot = 0
add = 0

for x in infile:
    x = x.rstrip()
    long = len('X-DSPAM-Confidence:')
    if x.startswith('X-DSPAM-Confidence:'):
        str = x
        num = float(str[long:])
        add = add + num
        tot = tot + 1
avg = add / tot
print('Average spam confidence: ', round(avg,12))