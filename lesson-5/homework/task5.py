#1.Determines whether a given year is a leap year.
year = int(input('Enter year: '))

def is_leap_year(year):
    result = False

    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:#it checks the year is leap or not
        result = True

    return result

print(is_leap_year(year))


# 2. Conditional Statements Exercise
# Given an integer, n, perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird
n = int(input('Enter a number: '))

if n % 2 == 1:
    print('Weird')
elif n % 2 == 0:
    if 2 <= n <= 5 or n > 20:
        print('Not Weird')
    elif 6 <= n <= 20:
        print('Weird')


#3.Given two integer numbers a and b. Find even numbers between this numbers. a and b are inclusive. Don't use loop.
# Give two solutions.

# Solution 1 with if-else statement.
# Solution 2 without if-else statement.

#first way with if-else
a1 = int(input('Enter start point a = '))
b1 = int(input('Enter end point b = '))

if b1 >= a1:
    if a1 % 2 != 0:
        a1 += 1
    even_numbers1 = list(range(a1, b1 + 1, 2))
    print(even_numbers1)
else:
    print('Please, enter correct numbres')


#second way without if-else
a2 = int(input('Enter start point a = '))
b2 = int(input('Enter end point b = '))

a2 += a2 % 2
even_numbers2 = list(range(a2, b2 + 1, 2))
print(even_numbers2)

