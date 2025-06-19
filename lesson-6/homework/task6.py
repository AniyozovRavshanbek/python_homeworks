# 1. Modify String with Underscores
# Given a string txt, insert an underscore (_) after every third character. If a character is a vowel or already has an underscore after it, shift the underscore placement to the next character. No underscore should be added at the end.
txt = input("Enter the string: ")
vowels = 'aeiou'

txt = list(txt)
i = 3

while i < len(txt):
    while i < len(txt) and (txt[i - 1] in vowels or (i < len(txt) and txt[i] == '_')):
        i += 1
    if i < len(txt):
        txt.insert(i, '_')
        i += 4  
    else:
        break
   
print(''.join(txt))



# 2. Integer Squares Exercise
# Task
# The provided code stub reads an integer, n, from STDIN. For all non-negative integers i where 0 <= i < n, print i^2.
n = int(input('Enter number: '))

for i in range(n):
    print(i**2)



# 3. Loop-Based Exercises
# Exercise 1: Print first 10 natural numbers using a while loop
i = 1

while i <= 10:
    print(i)
    i += 1


#Exercise 2: Print the following pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end = ' ')
    print()


# Exercise 3: Calculate sum of all numbers from 1 to a given number
n1 = int(input('Enter a number: '))
k = 0

for i in range(1, n1+1):
    k += i

print(k)


#Exercise 4: Print multiplication table of a given number
num = int(input('Enter a number: '))

for i in range(1, 11):
    print(num * i)


#Exercise 5: Display numbers from a list using a loop
# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the following number
# If the number is greater than 500, then stop the loop
numbers = [12, 75, 150, 180, 145, 525, 50]

for value in numbers:
    if value % 5 == 0:
        if value > 500:
            break
        elif value > 150:
            continue
        print(value)



#Exercise 6: Count the total number of digits in a number
number = int(input('Enter a number: '))
cnt = len(str(abs(number)))

print(f'The count of total digits in {number}: {cnt}')


#Exercise 7: Print reverse number pattern
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1
for i in range(5):
    for j in range(i + 1, 6):
        print(6-j, end = ' ')
    print()


#Exercise 8: Print list in reverse order using a loop
list1 = [10, 20, 30, 40, 50]

for i in range(1, len(list1) + 1):
    print(list1[-i])



#Exercise 9: Display numbers from -10 to -1 using a for loop
for i in range(-10, 0):
    print(i)



#Exercise 10: Display message “Done” after successful loop execution
num = int(input('Enter an end number of sequense: '))

for i in range(num):
    print(i)
else:
    print('Done')


#Exercise 11: Print all prime numbers within a range
m1 = int(input('Enter the first value of range: '))
m2 = int(input('Enter the second value of range: '))

for i in range(m1, m2 + 1):
    result = True
    if i > 1:
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                result = False
        if result:
            print(i)



#Exercise 12: Display Fibonacci series up to 10 terms
k = 0
fibo_list = [0, 1]

for i in range(1, 9):
    fibo_list.append(fibo_list[i] + fibo_list[i-1])

print('Fibonacci sequence:')
[print(x, end = ' ') for x in fibo_list]



#Exercise 13: Find the factorial of a given number
n1 = int(input('Enter a number to calculate factorial: '))
i = 1

for j in range(1, n1 + 1):
    i *= j

print(i)


#4. Return Uncommon Elements of Lists
# Task
# Return the elements that are not common between two lists. The order of elements does not matter.
list1 = list(map(int, input('Enter the first list elements: ').split()))
list2 = list(map(int, input('Enter the second list elements: ').split()))
list3 = []

for i in list1:
    if i not in list2:
        list3.append(i)

for j in list2:
    if j not in list1:
        list3.append(j)

print(list3)







    




        




