x = float(input("first number: "))
y = float(input("second number: "))
z = float(input("third number: "))

if (x > y and x > z):
    print(x, " is max")
elif(y > x and y > z):
    print(y, ' is max')
elif (z > x and z > y):
    print(z, ' is max')
    
if (x < y and x < z):
    print(x, 'is min')
elif (y < x and y < z):
    print(y, 'is min')
elif (z < x and z < y):
    print(z, 'is min')