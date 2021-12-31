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

weight = float(sys.argv[1])
height = float(sys.argv[2])

printresults(height, weight)  