import sys

def computepay(hours, rate):
    try:  
        if hours > 40:
            overtime = hours - 40
            overtimepay = (overtime) * (rate * 1.75)
            
            pay = overtimepay + (40 * rate)
            return 'Your gross pay is $' + str(pay) + '.'
        else:
            pay = hours * rate
            return 'Your gross pay is $' + str(pay) + '.'
    except:
        return ('You must put in numeric values or the program will not work. Please try again.')
        
hours = float(sys.argv[1])
rate = float(sys.argv[2])

print(computepay(hours, rate))