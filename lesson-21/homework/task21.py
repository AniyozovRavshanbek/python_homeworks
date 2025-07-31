import pandas as pd
import matplotlib.pyplot as plt

### DataFrame 1: Student Grades
data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

df1 = pd.DataFrame(data1)

# Exercise 1: Calculate the average grade for each student.
subjects = ['Math', 'English', 'Science']
df1['average_grade'] = df1[subjects].mean(axis=1).round(2)

print(df1['average_grade'])


# Exercise 2: Find the student with the highest average grade.
highest_avg_grade = df1['average_grade'].max()

print(df1[df1['average_grade'] == highest_avg_grade])


# Exercise 3: Create a new column 'Total' representing the total marks obtained by each student.
df1['Total'] = df1[subjects].sum(axis=1)

print(df1)

# Exercise 4: Plot a bar chart to visualize the average grades in each subject.
avg_grade = df1[subjects].mean()
sbj = avg_grade.index
grade = avg_grade.values

plt.bar(sbj, grade, width=0.5)
plt.xlabel('Subjects')
plt.ylabel('Average grades')
plt.title('Average grades by subjects')
plt.show()



### DataFrame 2: Sales Data
data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df2 = pd.DataFrame(data2)

# Exercise 1: Calculate the total sales for each product.
products = ['Product_A', 'Product_B', 'Product_C']
total_sales_per_product = df2[products].sum()

print(total_sales_per_product)


# Exercise 2: Find the date with the highest total sales.
df2['total_sales'] = df2[products].sum(axis=1)

print(df2[df2['total_sales'] == df2['total_sales'].max()][['Date', 'total_sales']])


# Exercise 3: Calculate the percentage change in sales for each product from the previous day.
percentage_change = (df2[products]/df2[products].shift(1).fillna(df2[products])*100 - 100).round(2)
print(percentage_change)


# Exercise 4: Plot a line chart to visualize the sales trends for each product over time.
plt.plot(df2['Date'], df2[products], label = ['Product A', 'Product B', 'Product C'])
plt.legend(title = 'Products')
plt.title('Product trends over time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.show()




### DataFrame 3: Employee Information
data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}

df3 = pd.DataFrame(data3)

# Exercise 1: Calculate the average salary for each department.
avg_salary = df3.groupby('Department')['Salary'].mean().round(2)

print(avg_salary)


# Exercise 2: Find the employee with the most experience.
max_experience = df3['Experience (Years)'].max()

print(df3[df3['Experience (Years)'] == max_experience])


# Exercise 3: Create a new column 'Salary Increase' representing the percentage increase in salary from the minimum salary in the dataframe.
df3['Salary Increase'] = round(df3['Salary']/df3['Salary'].min()*100 - 100, 2)

print(df3)


# Exercise 4: Plot a bar chart to visualize the distribution of employees across different departments.
employee_count = df3['Department'].value_counts()
plt.bar(employee_count.index, employee_count.values)
plt.title('Employee distribution by department')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.show()



### DataFrame 4: Customer Orders
data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}

df4 = pd.DataFrame(data4)


# Exercise 1: Calculate the total revenue from all orders.
total_revenue = df4['Total_Price'].sum()

print('Total revenue:', total_revenue)


# Exercise 2: Find the most ordered product.
most_order_pd = df4.groupby('Product')['Quantity'].sum()
max_value = most_order_pd.max()

print(most_order_pd[most_order_pd == max_value])


# Exercise 3: Calculate the average quantity of products ordered.
avg_quantity = df4.groupby('Product')['Quantity'].mean()

print(avg_quantity)


# Exercise 4: Plot a pie chart to visualize the distribution of sales across different products.
sales_by_product = df4.groupby('Product')['Total_Price'].sum()

plt.pie(sales_by_product.values, labels=sales_by_product.index)

plt.show()
