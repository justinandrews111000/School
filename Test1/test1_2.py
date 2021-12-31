import sys

name = sys.argv[1]
hips = int(sys.argv[2])


if hips < 91:
    size = 'XXSmall'
elif 91 <= hips < 96:
    size = 'XSmall'
elif 96 <= hips < 99:
    size = 'Small'
elif 99 <= hips < 103:
    size = 'Medium'
elif 103 <= hips < 107:
    size = 'Large'
elif hips > 107:
    size = 'XLarge'

print(name + ',', 'based on your hip size which is', hips, 'cm, your size is', size + '.')