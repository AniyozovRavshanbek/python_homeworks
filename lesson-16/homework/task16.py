import numpy as np
# # 1. Convert List to 1D Array

# Write a NumPy program to convert a list of numeric values into a one-dimensional NumPy array.

# Expected Output:

# Original List: [12.23, 13.32, 100, 36.32]
# One-dimensional NumPy array: [ 12.23 13.32 100. 36.32]
original_list = [12.23, 13.32, 100, 36.32]
list_to_array = np.array(original_list)

print(list_to_array)



# # 2. Create 3x3 Matrix (2?10)

# Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.

# Expected Output:

# [[ 2 3 4]
# [ 5 6 7]
# [ 8 9 10]]
array = np.arange(2, 11).reshape(3, 3)

print(array)



# # 3. Null Vector (10) & Update Sixth Value

# Write a NumPy program to create a null vector of size 10 and update the sixth value to 11.

# [ 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

# Update sixth value to 11
# [ 0. 0. 0. 0. 0. 0. 11. 0. 0. 0.]
null_vector = np.zeros(10)
null_vector[5] = 11

print(null_vector)



# # 4. Array from 12 to 38

# Write a NumPy program to create an array with values ranging from 12 to 38.

# Expected Output:

# [12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37]
numbers = np.arange(12, 38)

print(numbers)



# # 5. Convert Array to Float Type

# Write a NumPy program to convert an array to a floating type.

# Sample output:

# Original array
# [1, 2, 3, 4]
original_array = [1, 2, 3, 4]
to_float = np.array(original_array, float)

print(to_float)


# # 6. Celsius to Fahrenheit Conversion

# Write a NumPy program to convert Centigrade degrees into Fahrenheit degrees. Centigrade values are stored in a NumPy array.

# Sample Array [0, 12, 45.21, 34, 99.91, 32.]#missed 32. so I added 32.
# [-17.78, -11.11, 7.34, 1.11, 37.73, 0. ]

# Expected Output:

# Values in Fahrenheit degrees:
#  [ 0. 12. 45.21 34. 99.91 32. ]

# Values in Centigrade degrees:
# [-17.78 -11.11 7.34 1.11 37.73 0. ]

# Values in Centigrade degrees:
# [-17.78 -11.11 7.34 1.11 37.73 0. ]

# Values in Fahrenheit degrees:
# [-0. 12. 45.21 34. 99.91 32. ]

#Formula:
#C/5 = (F-32)/9
#C = 5*(F-32)/9
#F = (9*C + (32*5))/5
f_value1 = np.array([0, 12, 45.21, 34, 99.91, 32.])
c_value1 = np.round(5*(f_value1-32)/9, 2)

c_value2 = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0. ])
f_value2 = np.round((9*c_value2 + 160)/5, 2)

print(f'Values in Centigrade degrees: {c_value1}')
print(f'Values in Fahrenheit degrees: {f_value2}')



# # 7. Append Values to Array (Do self-tudy)

# Write a NumPy program to append values to the end of an array.

# Expected Output:

# Original array:
# [10, 20, 30]

# After append values to the end of the array:
# [10 20 30 40 50 60 70 80 90]
array_org = np.array([10, 20, 30])

appended_array = np.append(array_org, [40, 50, 60, 70, 80, 90])
print(appended_array)



# # 8. Array Statistical Functions (Do self-tudy)

# Create a random NumPy array of 10 elements and calculate the mean, median, and standard deviation of the array.
random_array = np.random.randint(1, 100, 10)

mean = np.mean(random_array)
median = np.median(random_array)
std = np.std(random_array)

print(f'Random array: {random_array}')
print(f'Mean: {mean}, Median: {median}, Standard Deviation: {std}')



# # 9 Find min and max 

# Create a 10x10 array with random values and find the minimum and maximum values.
rand_array = np.random.randint(1, 1000, 100).reshape(10, 10)

print(f'Minimum value: {rand_array.min()}  Maximum value: {rand_array.max()}')


# # 10 
# Create a 3x3x3 array with random values.
three_d_array = np.random.randint(1, 1000, 27).reshape(3, 3, 3)

print(three_d_array)
