#Dictionary Exercises
# 1. Sort a Dictionary by Value
# Write a Python script to sort (ascending and descending) a dictionary by value.
students_age = {'Alex':25, 'Emma':22, 'John':20, 'Leon':30}

#sorting in ascending order
ascending_order = dict(sorted(students_age.items(), key = lambda item:item[1]))
print(ascending_order)

#sorting in descending order
descending_order = dict(sorted(students_age.items(), key = lambda item:item[1], reverse=True))
print(descending_order)


# 2. Add a Key to a Dictionary
# Write a Python script to add a key to a dictionary.
numbers = {0: 10, 1: 20}

#the first way with key
numbers[2] = 30
print(numbers)

#the second way with update
numbers.update({3:40})
print(numbers)


# 3. Concatenate Multiple Dictionaries
# Write a Python script to concatenate the following dictionaries to create a new one.
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

numbers_dictionary = {}

for x in [dic1, dic2, dic3]:
    numbers_dictionary.update(x)

print(numbers_dictionary)


# 4. Generate a Dictionary with Squares
# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
n = int(input('Enter dictionary elements count: '))
numbers_square = {}

#creating by using x as a key
for x in range(1, n + 1):
    numbers_square[x] = x**2

print(numbers_square)


# 5. Dictionary of Squares (1 to 15)
# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
numbers_square1 = {}


for y in range(1, 16):
    numbers_square1[y] = y**2

print(numbers_square1)



# Set Exercises
# 1. Create a Set
# Write a Python program to create a set.

#with set function
fruits = set(('apple', 'banana', 'orange', 'cherry', 'peach'))
print(fruits)

#with just curly brackets
fruits_set = {'apple', 'banana', 'orange', 'cherry', 'peach'}
print(fruits_set)



# 2. Iterate Over a Set
# Write a Python program to iterate over sets.
numbers_set = {1, 4, 5, 6.7, 8, -4.5}
for x in numbers_set:
    print(x)



# 3. Add Member(s) to a Set
# Write a Python program to add member(s) to a set.
laptop_brands = {'macbook', 'lenovo', 'acer', 'hp', 'asus'}

#using by add() method
laptop_brands.add('huawei')
print(laptop_brands)


# 4. Remove Item(s) from a Set
# Write a Python program to remove item(s) from a given set.
phone_brands = {'iphone', 'samsung', 'oppo', 'xiaomi', 'pixel'}

#using remove() method
phone_brands.remove('iphone')#it returns error if there isn't item which in remove() method
print(phone_brands)


# 5. Remove an Item if Present in the Set
# Write a Python program to remove an item from a set if it is present in the set.
programming_languages = {'Python', 'Java', 'C', 'C++', 'PHP', 'Rust', 'GO', 'JavaScript'}

#using discard() method
programming_languages.discard('PHP')
print(programming_languages)





