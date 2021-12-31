g1 = float(input('What is your 1st grade: '))
g2 = float(input('What is your 2nd grade: '))
g3 = float(input('What is your 3rd grade: '))
g4 = float(input('What is your 4th grade: '))

avg = round((g1+g2+g3+g4)/4, 2)

grades = ('Grades: {:.2f}, {:.2f}, {:.2f}, {:.2f}').format(g1, g2, g3, g4)
print(grades)
print('Average:',avg)