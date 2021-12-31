'''
Created on Dec 6, 2021

@author: justi
'''
def calc_add():
    with open(r"C:\Users\justi\Downloads\concerts.txt", 'r') as myfile:
        
        Calypso = 0
        BluesBBQ = 0
        Bluegrass = 0
        
        for line in myfile:

            endIdxC = line.find('\',ticket')
            startIdxS = line.find('$') + 1
            
            concert = line[9 : endIdxC]
            
            if concert == 'Bluegrass Festival':
                sales = int(line[startIdxS:])
                Bluegrass += sales
            
            elif concert == 'Blues & BBQ':
                sales = int(line[startIdxS:])
                BluesBBQ += sales
            elif concert == 'Calypso':
                sales = int(line[startIdxS:])
                Calypso += sales
        print('------Ticket Sales------')
        print('Bluegrass Festival, ${}'.format(round(Bluegrass, 2)))
        print('Blues & BBQ, ${}'.format(round(BluesBBQ, 2)))
        print('Calypso, ${}'.format(round(Calypso, 2)))
        print('------------------------')
            
calc_add()
            
            
    
    
        