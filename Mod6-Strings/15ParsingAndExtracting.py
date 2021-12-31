'''
Created on Nov 14, 2021
'''

data ='From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 20'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ', atpos)
print(sppos)

host = data[atpos + 1 : sppos]
print(host)