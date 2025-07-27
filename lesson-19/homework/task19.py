import pandas as pd
# **Homework Assignment 1: Analyzing Sales Data**

# You are given a dataset containing sales data for an e-commerce website. The dataset (`task\sales_data.csv`) has the following columns:

# - `Date`: Date of the sale.
# - `Product`: Name of the product sold.
# - `Category`: Category to which the product belongs.
# - `Quantity`: Number of units sold.
# - `Price`: Price per unit.

# **Tasks:**
sales = pd.read_csv(r'19-lesson\sales_data.csv')

# 1. Group the data by the `Category` column and calculate the following aggregate statistics for each category:
#    - Total quantity sold.
#    - Average price per unit.
#    - Maximum quantity sold in a single transaction.
data = sales.groupby('Category').agg(
    total_sold_quantity = ('Quantity', 'sum'),
    average_price = ('Price', 'mean'),
    max_quantity = ('Quantity', 'max'),
).reset_index()

print(data)


# 2. Identify the top-selling product in each category based on the total quantity sold.
grouped = sales.groupby(['Category', 'Product']).agg(
    total_sold_quantity = ('Quantity', 'sum')
).reset_index()
grouped['max_in_category'] = grouped.groupby('Category')['total_sold_quantity'].transform('max')

print(grouped[grouped['total_sold_quantity'] == grouped['max_in_category']].drop(columns='max_in_category'))


# 3. Find the date on which the highest total sales (quantity * price) occurred.
sales['total_sales'] = sales['Quantity'] * sales['Price']

sum_values = sales.groupby('Date')['total_sales'].sum().reset_index()
max_value = sum_values['total_sales'].max()
print(sum_values[sum_values['total_sales'] == max_value])



# **Homework Assignment 2: Examining Customer Orders**

# You have a dataset (`task\customer_orders.csv`) containing information about customer orders. The dataset has the following columns:

# - `OrderID`: Unique identifier for each order.
# - `CustomerID`: Unique identifier for each customer.
# - `Product`: Name of the product ordered.
# - `Quantity`: Number of units ordered.
# - `Price`: Price per unit.

# **Tasks:**
orders = pd.read_csv('19-lesson\customer_orders.csv')

# 1. Group the data by `CustomerID` and filter out customers who have made less than 20 orders.
grouped = orders.groupby('CustomerID')['OrderID'].count().reset_index()
customer_id = grouped[grouped['OrderID'] < 20]['CustomerID'].values

print(orders[orders['CustomerID'].isin(customer_id)])


# 2. Identify customers who have ordered products with an average price per unit greater than $120.
data = orders.groupby('CustomerID')['Price'].mean().reset_index()
filt = data[data['Price'] > 120]['CustomerID'].values

print(orders[orders['CustomerID'].isin(filt)])


# 3. Find the total quantity and total price for each product ordered, and filter out products that have a total quantity less than 5 units.
orders['Total'] = orders['Quantity'] * orders['Price']

total = orders.groupby('Product').agg(
    total_quantity = ('Quantity', 'sum'),
    total_price = ('Total', 'sum')
).reset_index()

print(total[total['total_quantity'] < 5])




# **Homework Assignment 3: Population Salary Analysis**

# 1. "task\population.db" sqlite database has `population` table.
import sqlite3

connection = sqlite3.connect('19-lesson\population.db')
select_query = 'select * from population'

population = pd.read_sql_query(select_query, connection)


# 2. "task\population salary analysis.xlsx" file defines Salary Band categories.
#     Read the data from population table and calculate following measures:
#     - Percentage of population for each salary category;
#     - Average salary in each salary category;
#     - Median salary in each salary category;
#     - Number of population in each salary category;
salary_band = pd.read_excel('19-lesson\population_salary_analysis.xlsx', sheet_name='Salary band')

bins = [-float('inf'), 200000, 400000, 600000, 800000, 1000000,
        1200000, 1400000, 1600000, 1800000, float('inf')]
labels = salary_band['Salary Band'].values


population["Salary Band"] = pd.cut(population["salary"], bins=bins, labels=labels, right=True)

statistics = population.groupby('Salary Band').agg(
    average_salary = ('salary', 'mean'),
    median_salary = ('salary', 'median'),
    number_of_population = ('id', 'count'),
).reset_index().round(2)

statistics['percentage_of_people'] = (statistics['number_of_population']/population['id'].count()*100).round(2).astype('str') + '%'

print(statistics)


# 3. Calculate the same measures in each State
statistics_by_state = population.groupby('state').agg(
    average_salary = ('salary', 'mean'),
    median_salary = ('salary', 'median'),
    number_of_population = ('id', 'count'),
).reset_index().round(2)

statistics_by_state['percentage_of_people'] = (statistics_by_state['number_of_population']/population['id'].count()*100).round(2).astype('str') + '%'

print(statistics_by_state)



# Note: Use SQL only to select data from database. All the other calculations should be done in python.


