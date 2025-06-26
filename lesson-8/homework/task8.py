#Exception Handling Exercises
#1.Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
try:
    print(4/5)
    print(10/0)
except ZeroDivisionError:
    print("Dividing 0 is wrong")


#2.Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
try:
    a = int(input('Enter an integer number: '))
    print(a)
except ValueError:
    raise ValueError("This isn't valid integer")


#3.Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
try:
    f = open('file1.txt')
    print(f.read())
except FileNotFoundError:
    print('The file does not exist')


#4.Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.
try:
    num1 = float(input('Enter number1: '))
    num2 = float(input('Enter number2: '))
    print(num1, num2)
except ValueError:
    raise TypeError('The values must be numerical')


#5.Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.
try:
    f = open('file5.txt',)
    print(f.read())
except PermissionError:
    print('Sorry, it seems like you have not permission')


#6.Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.
try:
    fruits = ['apple', 'banana', 'lemon']
    print(fruits[1])
    print(fruits[5])
except IndexError:
    print('Please, check index number!')


#7.Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.
try:
    number = float(input('Input any number: '))
    print(number)
except KeyboardInterrupt:
    print('Input cancelled by user')


#8.Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.
value1 = float(input('Enter first value: '))
value2 = float(input('Enter second value: '))

#ZeroDivisionError
try:
    print(value1/value2)
except ArithmeticError:
    print('Please sure your values are right or not')

#OverflowError
import math
try:
    print(math.exp(1000))
except ArithmeticError:
    print('It seems like numerical operation exceeds the limits of the numeric type')


#9.Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue.
with open('file1.txt', 'w', encoding='utf-8') as f:
    f.write('Hello, this is a testing message 😊')

try:
    with open('file1.txt', encoding='ascii') as f:
        print(f.read())
except UnicodeDecodeError:
    print('It seems like there is an encoding issue. Please check encoding')


#10.Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.
try:
    text = 'Hello everbody'
    print(text.upper())
    print(text.append())
except AttributeError:
    print('Please check attribute you used')



# File Input/Output Exercises
# 1.Write a Python program to read an entire text file.
try: 
    with open('file1.txt') as f:
        print(f.read())
except FileNotFoundError:
    print('Check file path')


# 2.Write a Python program to read first n lines of a file.
n = int(input('Enter lines number of file you want to see: '))

if n <= 0:
    print('Please enter obvious value')
else:
    try:
        with open('file2.txt') as f:
            for i in f.readlines()[:n]:
                print(i.strip())
    except FileNotFoundError:
        print('Check the file path or create a new file')
    
        
# 3.Write a Python program to append text to a file and display the text.
with open('file3.txt', 'a') as f:
    f.write("I'm a BI developer\n")

with open('file3.txt') as fr:
    print(fr.read())


# 4.Write a Python program to read last n lines of a file.
m = int(input('Enter a number to see last n lines of a file: '))

if m <= 0:
    print('Please input obvious value')
else:
    try:
        with open('file2.txt') as f:
            for i in f.readlines()[-m:]:
                print(i.strip())
    except FileNotFoundError:
        print('Check the file path or create a new file')


# 5.Write a Python program to read a file line by line and store it into a list.
try:
    with open('file2.txt') as f:
        l = f.readlines()
        print(l)
except FileNotFoundError:
    print('Check the file path or create a new file')


# 6.Write a Python program to read a file line by line and store it into a variable.
try:
    with open('file2.txt') as f:
        a = ''
        
        for i in f.readlines():
            a += i
        print(a)
except FileNotFoundError:
    print('Check the file path or create a new file')


# 7.Write a Python program to read a file line by line and store it into an array.
try:
    with open('file2.txt') as f:
        l1 = [i for i in f.readlines()]
        print(l1)
except FileNotFoundError:
    print('Check the file path or create a new file')


# 8.Write a Python program to find the longest words.
with open('file2.txt') as f:
    words = f.read().split()
    max_len = max(len(word) for word in words)
    longest_words = {word for word in words if len(word) == max_len}

print(*longest_words, sep='\n')


# 9.Write a Python program to count the number of lines in a text file.
try:
    with open('file2.txt') as f:
        k = 0

        for i in f.readlines():
            k += 1
except FileNotFoundError:
    print('Check the file path or create a new file')

print(k)


# 10.Write a Python program to count the frequency of words in a file.
try:
    with open('file2.txt') as f:
        a = f.read().split()
        b = set(a)
    
        for i in b:
            print(f"{i} - {a.count(i)}")
except FileNotFoundError:
        print('Check the file path or create a new file')


# 11.Write a Python program to get the file size of a plain file.
from os import path

file = 'file2.txt'
print(f'File size is {path.getsize(file)} bytes')


# 12.Write a Python program to write a list to a file.
with open('fruits.txt', 'w') as f:
    fruits = ['apple', 'banana', 'cherry', 'lemon', 'grape']
    fruits_str = ','.join(fruits) + '\n'
    f.write(fruits_str)

with open('fruits.txt') as f:
    print(f.read())


# 13.Write a Python program to copy the contents of a file to another file.
with open('file2.txt') as f, open('file.txt', 'a') as file:
    file.write(f.read())


# 14.Write a Python program to combine each line from the first file with the corresponding line in the second file.
with open('file2.txt') as f, open('file3.txt') as file:
    for i, j in zip(f.readlines(), file.readlines()):
        print(f'{i.strip()} : {j.strip()}')


# 15.Write a Python program to read a random line from a file.
import random

with open('file2.txt') as f:
    a = f.readlines()
    length = len(a)

    rand = random.randint(0, length-1)
    print(a[rand])


# 16.Write a Python program to assess if a file is closed or not.
f = open('file2.txt')
f.close()

if f.closed:
    print('The file closed')
else:
    print('It seems like you have not closed the file')


# 17.Write a Python program to remove newline characters from a file.
with open('file2.txt') as f:
    text = f.read()
    result = text.replace('\n', '')

with open('cleaned_file2.txt', 'w') as f:
    f.write(result)


# 18.Write a Python program that takes a text file as input and returns the number of words in a given text file.
# Note: Some words can be separated by a comma with no space.
with open('test_file.txt', 'w') as f:
    f.write(input('Enter a text: '))

with open('test_file.txt') as f:
    txt = f.read().replace(',', ' ')
    
    print(len(txt.split()))


# 19.Write a Python program to extract characters from various text files and put them into a list.
files = ['file1.txt', 'file2.txt', 'file3.txt']
characters_list = []

for i in files:
    with open(i) as f:
        for i in f.read():
            characters_list.append(i)

print(characters_list)


# 20.Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.
a = ord('A')
b = ord('Z')

for i in range(a, b + 1):
    f = open(f'{chr(i)}.txt', 'w')


# 21.Write a Python program to create a file where all letters of the English alphabet are listed with a specified number of letters on each line.
first_lt = ord('A')
last_lt = ord('Z')
k = 1

for i in range(first_lt, last_lt + 1):
    with open('letters.txt', 'a') as f:
        l = map(str, [chr(i), k])
        result = ','.join(l) + '\n'

        f.write(result)
        k += 1

    
