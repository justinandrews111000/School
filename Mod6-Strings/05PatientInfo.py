
patientInfo = input('Please enter patient info in the following format [Name, Age, Cholesterol category, height, weight.]: ')

infoList = patientInfo.split(',')

dcount = 0
bcount = 0
hcount = 0

for i in infoList:
    if i == 'desirable':
        dcount += 1
    elif i == 'borderline':
        bcount += 1
    elif i == 'high':
        hcount += 1
    else:
        continue
print('Desireable count: {}'.format(dcount))
print('Borderline count: {}'.format(bcount))
print('High count: {}'.format(hcount))   
    