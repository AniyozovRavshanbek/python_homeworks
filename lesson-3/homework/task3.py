# 1. Create and Access List Elements
# Create a list containing five different fruits and print the third fruit.
fruits = ['apple', 'cherry', 'orange', 'banana', 'peach']
print(fruits[2])#it returns the third fruit


# 2. Concatenate Two Lists
# Create two lists of numbers and concatenate them into a single list.
numbers1 = [1, 4, 100, -5.6]
numbers2 = [99, 67, 4.3, 90, 105]

#the first way with +
numbers = numbers1 + numbers2
print(numbers)

#the second way with extend()
numbers1.extend(numbers2)
print(numbers1)


# 3. Extract Elements from a List
# Given a list of numbers, extract the first, middle, and last elements and store them in a new list.
numbers_list = list(map(float, input('Enter numbers: ').split()))
n = len(numbers_list)

first = numbers_list[0]
middle = numbers_list[n // 2]
last = numbers_list[-1]

new_list = [first, middle, last]

print('Result:', new_list)


# 4. Convert List to Tuple
# Create a list of your five favorite movies and convert it into a tuple.
movies = ['Harry Potter', 'Green Destination', 'Forrest Gump', 'Equalizer I', 'Equalizer II']
movies_as_tuple = tuple(movies)#tuple function returns data as a tuple data type

print(movies_as_tuple)


# 5. Check Element in a List
# Given a list of cities, check if "Paris" is in the list and print the result.
cities = input('Enter cities with space: ').split()
result = False

for city in cities:
    if city.capitalize() == 'Paris':
        result = True

if result:
    print('Yes, Paris is in the list')
else:
    print('No, Paris is not in the list')



# 6. Duplicate a List Without Using Loops
# Create a list of numbers and duplicate it without using loops.

#duplicating with * operator
numbers_list = [1, 3, 10, 98, 4.5, -3]
numbers_list *= 2

print(numbers_list)


# 7. Swap First and Last Elements of a List
# Given a list of numbers, swap the first and last elements.
list_of_numbers = list(map(float, input('Enter numbers: ').split()))

list_of_numbers[0], list_of_numbers[-1] = list_of_numbers[-1], list_of_numbers[0]

print(list_of_numbers)


# 8. Slice a Tuple
# Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.
numbers_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(numbers_tuple[3:7])

# 9. Count Occurrences in a List
# Create a list of colors and count how many times "blue" appears in the list.
colors = ['yellow', 'White', 'Blue', 'PINK', 'black', 'BLUE', 'white', 'blue']
k = 0

for color in colors:
    if color.lower() == 'blue':
        k += 1

print(k)


# 10. Find the Index of an Element in a Tuple
# Given a tuple of animals, find the index of "lion".
animal = tuple(input('Enter animals: ').split())
m = False

for i in range(len(animal)):
    if animal[i].lower() == 'lion':
        m = True
        print(f'{i}', end = ' ')

if not m:
    print('lion not found')


# 11. Merge Two Tuples
# Create two tuples of numbers and merge them into a single tuple.
numbers_tuple1 = (10, 40, 3, 4.5, -9, 0, 0.45, 1.34, 12, 15)
numbers_tuple2 = (35, 400, 45, 3.2, 877, 9.34, -45, -34, 56, 78)

merged_tuple = numbers_tuple1 + numbers_tuple2

print(merged_tuple)


# 12. Find the Length of a List and Tuple
# Given a list and a tuple, find and print their lengths
laptop_brands = list(input('Enter laptop brand with space: ').split())
telephone_brands = tuple(input('Enter telephone brand with space: ').split())

print(f'The length of the list: {len(laptop_brands)}')
print(f'The length of the tuple: {len(telephone_brands)}')


# 13. Convert Tuple to List
# Create a tuple of five numbers and convert it into a list.
nums = (3, 5, 10, 45, 5.6, -4)
nums_list = list(nums)#list function converts tuple into list here

print(nums_list)


# 14. Find Maximum and Minimum in a Tuple
# Given a tuple of numbers, find and print the maximum and minimum values.
nums_tuple = tuple(map(float, input('Enter numbers: ').split()))

#max and min functions return max and min value in the tuple 
print(f'Max value: {max(nums_tuple)}   Min value: {min(nums_tuple)}')


# 15. Reverse a Tuple
# Create a tuple of words and print it in reverse order.
words = ('orange', 'white', 'hello', 'bye', 'BMW', 'plane', 'apple')

#with reversed() function
reversed_words = tuple(reversed(words))

print('Result:', reversed_words)

#with slicing
print('Result:', words[::-1])

