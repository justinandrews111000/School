grade = float(input('Please enter a grade within the range of 0 to 1: '))

if 0 <= grade <= 1: 
    if grade >= 0.9:
        letter = 'A'
    elif grade >= 0.8:
        letter = 'B'
    elif grade >= 0.7:
        letter = 'C'
    elif grade >= 0.6:
        letter = 'D'
    elif grade < 0.6:
        letter = 'F'
    print('Your number grade is', grade * 100, 'and your letter grade is a(n)', letter)
else:
    print('Your numeric grade must be within the range of 0 to 1. Please enter a valid grade.')