import math
#1.Given a side of square. Find its perimeter and area.
a = float(input('Enter the side of square: '))
P, S = 4*a, a**2

print(f'Perimeter: {P} Area: {S}')

#2.Given diameter of circle. Find its length.
d = float(input('Enter the diameter of circle: '))
L = round(d*math.pi, 2)

print(f'The length of the circle: {L}')

#3.Given two numbers a and b. Find their mean.
a = float(input('Enter the first number: '))
b = float(input('Enter the second number: '))
mean = (a + b)/2

print('Mean:', mean)

#4.Given two numbers a and b. Find their sum, product and square of each number.
a = float(input('Enter the first number: '))
b = float(input('Enter the second number: '))

sum, product = a + b, a * b
square_a, square_b = a**2, b**2

print(f'Sum: {sum} Product: {product}')
print(f'Square of {a}: {square_a} Square of {b} = {square_b}')
