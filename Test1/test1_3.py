import sys

try:
    name = sys.argv[1]
    course = sys.argv[2]
    grade = int(sys.argv[3])
    courseID = sys.argv[4]

    
    if grade >= 70:
        print(name + ', ' + 'you have passed', courseID + '.')
    else:
        print(name + ', ' + 'you have failed', course + '.')
except:
    print('Course score must be entered as a number.')