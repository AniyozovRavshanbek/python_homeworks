# Homework 1:
import pandas as pd
import numpy as np

data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

# 1. Rename column names using function. "First Name" --> "first_name", "Age" --> "age
df.rename(columns={'First Name':'first_name', 'Age':'age'}, inplace=True)
print(df)


# 2. Print the first 3 rows of the DataFrame
print(df.head(3))

# 3. Find the mean age of the individuals
mean = df['age'].mean()
print('Age mean:', mean)

# 4. Select and print only the 'Name' and 'City' columns
print(df[['first_name', 'City']])

# 5. Add a new column 'Salary' with random salary values
df['Salary'] = np.random.randint(50000, 150000, df['age'].count())
print(df)

# 6. Display summary statistics of the DataFrame
print(f'Summary statistics\n{df.describe()}')



# Homework 2:

# 1. Create a DataFrame named sales_and_expenses with columns 'Month', 'Sales', and 'Expenses', representing monthly sales and expenses data.
# Use below table.

# | Month | Sales | Expenses |
# |-------|-------|----------|
# | Jan   | 5000  | 3000     |
# | Feb   | 6000  | 3500     |
# | Mar   | 7500  | 4000     |
# | Apr   | 8000  | 4500     |
data1 = {
    'Month':['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales':[5000, 6000, 7500, 8000],
    'Expenses':[3000, 3500, 4000, 4500]
}

sales_and_expenses = pd.DataFrame(data1)

# 2. Calculate and display the maximum sales and expenses.
max_sales = sales_and_expenses['Sales'].max()
max_expenses = sales_and_expenses['Expenses'].max()

print(f'Max sales: {max_sales}\nMax expenses: {max_expenses}')

# 3. Calculate and display the minimum sales and expenses.
min_sales = sales_and_expenses['Sales'].min()
min_expenses = sales_and_expenses['Expenses'].min()

print(f'Min sales: {min_sales}\nMin expenses: {min_expenses}')

# 4. Calculate and display the average sales and expenses.
average_sales = sales_and_expenses['Sales'].mean()
average_expenses = sales_and_expenses['Expenses'].mean()

print(f'Average sales: {average_sales}\nAverage expenses: {average_expenses}')



# Homework 3:

# 1. Create a DataFrame named expenses with columns 'Category', 'January', 'February', 'March', and 'April', representing monthly expenses for different categories. Use below table.

# | Category       | January | February | March | April |
# |----------------|---------|----------|-------|-------|
# | Rent           | 1200    | 1300     | 1400  | 1500  |
# | Utilities      | 200     | 220      | 240   | 250   |
# | Groceries      | 300     | 320      | 330   | 350   |
# | Entertainment  | 150     | 160      | 170   | 180   |

expenses = {
    'Category':['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January':[1200, 200, 300, 150],
    'February':[1300, 220, 320, 160],
    'March':[1400, 240, 330, 170],
    'April':[1500, 250, 350, 180]
}

expenses_df = pd.DataFrame(expenses)


# 2. Calculate and display the maximum expense for each category.
#we can use set_index() to solve the problem
expenses_df.set_index('Category', inplace=True)

max_expense = expenses_df.max(axis=1)

print(f'Maximum expense for each category:\n{max_expense}')

# 3. Calculate and display the minimum expense for each category.
min_expense = expenses_df.min(axis=1)

print(f'Minimum expense for each category:\n{min_expense}')

# 4. Calculate and display the average expense for each category.
average_expense = expenses_df.mean(axis=1)

print(f'Average expense for each category:\n{average_expense}')


# In this task, use `.set_index` method to make Category column as index. 

# Try this code, learn it and use it in the task.

# > expenses.set_index('Category')
