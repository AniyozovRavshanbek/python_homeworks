#Homework 2
import pandas as pd

df = pd.read_csv('18-lesson/stackoverflow_qa.csv')

# 1.Find all questions that were created before 2014
print(df[pd.to_datetime(df['creationdate']) < '2014'])


# 2.Find all questions with a score more than 50
print(df[df['score'] > 50])


# 3.Find all questions with a score between 50 and 100
print(df[df['score'].between(50, 100)])


# 4.Find all questions answered by Scott Boston
print(df[df['ans_name'] == 'Scott Boston'])


# 5.Find all questions answered by the following 5 users
# I haven't found any following 5 users here so I must choose the 5 users and filter by it
# Demitri, doug, Mike Pennington, Jubbles, DSM
print(df[df['ans_name'].isin(['Demitri', 'doug', 'Mike Pennington', 'Jubbles', 'DSM'])])


# 6.Find all questions that were created between March, 2014 and October 2014 that were answered by Unutbu and have score less than 5.
to_date = pd.to_datetime(df['creationdate'])
filt = (to_date.between('2014-03', '2014-10')) & (df['ans_name'] == 'Unutbu') & (df['score'] < 5)

print(df[filt])


# 7.Find all questions that have score between 5 and 10 or have a view count of greater than 10,000
filt = (df['score'].between(5, 10)) | (df['viewcount'] > 10000)

print(df[filt])


# 8.Find all questions that are not answered by Scott Boston
print(df[df['ans_name'] != 'Scott Boston'])



#Homework 3
import pandas as pd

titanic = pd.read_csv('18-lesson/titanic.csv')

# 1.Select Female Passengers in Class 1 with Ages between 20 and 30: Extract a DataFrame containing female passengers in Class 1 with ages between 20 and 30.
filt = (titanic['Sex'] == 'female') & (titanic['Pclass'] == 1) & (titanic['Age'].between(20, 30))

print(titanic[filt])


# 2.Filter Passengers Who Paid More than $100: Create a DataFrame with passengers who paid a fare greater than $100.
print(titanic[titanic['Fare'] > 100])


# 3.Select Passengers Who Survived and Were Alone: Filter passengers who survived and were traveling alone (no siblings, spouses, parents, or children).
filt = (titanic['Survived'] == 1) & ((titanic['SibSp'] == 0) & (titanic['Parch'] == 0))

print(titanic[filt])


# 4.Filter Passengers Embarked from 'C' and Paid More Than $50: Create a DataFrame with passengers who embarked from 'C' and paid more than $50.
filtered_df = titanic[(titanic['Embarked'] == 'C') & (titanic['Fare'] > 50)]

print(filtered_df)


# 5.Select Passengers with Siblings or Spouses and Parents or Children: Extract passengers who had both siblings or spouses aboard and parents or children aboard.
filt = (titanic['SibSp'] > 0 ) & (titanic['Parch'] > 0)

print(titanic[filt])


# 6.Filter Passengers Aged 15 or Younger Who Didn't Survive: Create a DataFrame with passengers aged 15 or younger who did not survive.
filtered_df = titanic[(titanic['Age'] <= 15) & (titanic['Survived'] == 0)]

print(filtered_df)


# 7.Select Passengers with Cabins and Fare Greater Than $200: Extract passengers with known cabin numbers and a fare greater than $200.
filt = (titanic['Cabin'].notna())  & (titanic['Fare'] > 200)

print(titanic[filt])


# 8.Filter Passengers with Odd-Numbered Passenger IDs: Create a DataFrame with passengers whose PassengerId is an odd number.
filtered_df = titanic[titanic['PassengerId']%2 != 0]

print(filtered_df)


# 9.Select Passengers with Unique Ticket Numbers: Extract a DataFrame with passengers having unique ticket numbers.
ticket_counts = titanic['Ticket'].value_counts()

ticket_index = ticket_counts[ticket_counts == 1].index

print(titanic[titanic['Ticket'].isin(ticket_index)])


# 10.Filter Passengers with 'Miss' in Their Name and Were in Class 1: Create a DataFrame with female passengers having 'Miss' in their name and were in Class 1.
filt = (titanic['Name'].str.contains('Miss')) & (titanic['Pclass'] == 1)

print(titanic[filt])
