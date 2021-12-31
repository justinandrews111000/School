num = int(input())



def Deci2Bin(num):
    while num > 0:
        temp = num % 2
        num = num // 2 
        print(temp, end = '')
        
if num > 1:
    Deci2Bin(num)
