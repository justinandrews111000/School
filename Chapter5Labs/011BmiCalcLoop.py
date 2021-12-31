import sys

def calcbmi(weight, height):
    
    bmi = round((weight/(height*height))*703, 2)
    
    return bmi

def getcategory(bmi):
    if bmi <= 18.5:
        category = 'Underweight'
    elif 18.5 < bmi <= 24.9:
        category = 'Normal Weight'
    elif 25.0 <= bmi <= 25.9:
        category = 'Overweight'
    elif 30.0 <= bmi <= 39.9:
        category = 'Obese'
    elif bmi >= 40:
        category = 'Extremely Obese'
        
    return category

def printresults(height, weight):
    print('BMI: {}, and the category is {}'.format(calcbmi(height, weight), getcategory(calcbmi(height, weight))))


inputlen = len(sys.argv) - 1

if inputlen % 2 != 0:
    print('You must enter the numbers in pairs.')
    print(inputlen)
else:
    
    weight = 0
    height = 0
    
    cont = 0
    
    for i in range(1, inputlen + 1):
        
        cont += 1

        num = float(sys.argv[i])
        
        if cont % 2 == 0:
            
            weight = num
            print('Weight: {}'.format(weight))
            printresults(weight, height)
            
        else:
            height = num
            print('Height: {}'.format(height))