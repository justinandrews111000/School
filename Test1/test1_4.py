import sys
try:
    name = sys.argv[1]
    m1 = int(sys.argv[2])
    m2 = int(sys.argv[3])
    m3 = int(sys.argv[4])
    m4 = int(sys.argv[5])
    
    avg = float((m1 + m2 + m3 + m4) / 4)
    
    if avg >= 4:
        print(name, 'shops on average', avg, 'times per month, and', name, 'is a super shopper.')
    else:
        print(name, 'shops on average', avg, 'times per month.')

except:
    print('Invalid Data.')