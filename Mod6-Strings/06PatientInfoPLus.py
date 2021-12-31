'''
Created on Nov 13, 2021
'''
def getcategory(bmi):
    bcategory = 'Default'
    if bmi <= 18.5:
        bcategory = 'Underweight'
    elif 18.5 < bmi <= 24.9:
        bcategory = 'Normal Weight'
    elif 25.0 <= bmi <= 29.9:
        bcategory = 'Overweight'
    elif 30.0 <= bmi <= 39.9:
        bcategory = 'Obese'
    elif bmi >= 40:
        bcategory = 'Extremely Obese'
    else:
        bcategory ='Off the charts'
       
    return bcategory



def calcbmi(weight, height):
    
    bmi = round((weight/(height*height))*703, 2)
    
    return bmi



patientInfo = input('Please enter patient info in the following format [Name, Age, Cholesterol category, height, weight.]: ')

infoList = patientInfo.split(',')
dcount = 0
bcount = 0
hcount = 0
count = 0

for i in infoList:
    count += 1
    if i == 'desirable':
        dcount += 1
    elif i == 'borderline':
        bcount += 1
    elif i == 'high':
        hcount += 1
    elif count == 1:
        name = i
    elif count == 4:
        height = int(i)
    elif count == 5:
        weight = int(i)
        count = 0
        bmi = float(calcbmi(weight, height))
        cate = getcategory(float(bmi))
        print('{}: {}, {}'.format(name, bmi, cate))

print('--------')
print('Desireable count: {}'.format(dcount))
print('Borderline count: {}'.format(bcount))
print('High count: {}'.format(hcount)) 
  
    
    