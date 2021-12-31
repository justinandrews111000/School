import sys

name = sys.argv[1]
price = float(sys.argv[2])
discount = int(sys.argv[3])

discountedPrice = price - (price * (discount/100))

discountedPrice = round(discountedPrice, 2)

print(name + ', the product price after taking the discount is $' + str(discountedPrice))