# 1. Age Calculator
# Write a Python program to ask for a user's name and year of birth, then calculate and display their age.
from datetime import datetime as d
name = input('Enter your name: ')
birth_year = int(input('Enter your year of birth: '))

age = d.now().year - birth_year

print(f"{name}'s age is {age}")


# 2. Extract Car Names
# Extract car names from the following text:
txt = 'LMaasleitbtui'

print(txt[::2], txt[1::2])


# 3. Extract Car Names
# Extract car names from the following text:
car_name = 'MsaatmiazD'

print(car_name[::2], car_name[::-2])


# 4. Extract Residence Area
# Extract the residence area from the following text:
msg = "I'am John. I am from London"

print(msg[-6:])


# 5. Reverse String
# Write a Python program that takes a user input string and prints it in reverse order.
text = input('Enter any text or word: ')

print(text[::-1])


# 6. Count Vowels
# Write a Python program that counts the number of vowels in a given string.
a = input('Enter any text or word: ')
vowels = 'aeiou'
k = 0

for x in a.lower():
    if x in vowels:
        k+= 1

print(k)


# 7. Find Maximum Value
# Write a Python program that takes a list of numbers as input and prints the maximum value.
numbers = list(map(float, input('Enter numbers: ').split()))

print(f'Max value: {max(numbers)}')


# 8. Check Palindrome
# Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).
word = input('Enter value: ')

if word.lower() == word[::-1].lower():
    print(f'{word} is palindrome')
else:
    print(f'{word} is not palindrome')


# 9. Extract Email Domain
# Write a Python program that extracts and prints the domain from an email address provided by the user.
email = input('Enter your email: ')

print(email[email.rfind('@')+1:])


# 10. Generate Random Password
# Write a Python program to generate a random password containing letters, digits, and special characters.
import secrets
import string

length = int(input('Enter password length: '))
alphabet = string.ascii_letters + string.digits + string.punctuation
password = ''.join(secrets.choice(alphabet) for i in range(length))

print(password)

