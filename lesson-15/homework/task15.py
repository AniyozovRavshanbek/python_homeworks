# ### Review Exercises

# 1. Create a new database with a table named Roster that has three fields: Name, Species, and Age. The Name and Species columns should be text fields, and the Age column should be an integer field.
import sqlite3

connection = sqlite3.connect('15-lesson/my_db.sqlite3')

cursor = connection.cursor()

create_query = 'create table if not exists Roster (Name varchar(50), Species varchar(50), Age int)'

cursor.execute(create_query)


# 2.  Populate your new table with the following values:

# | Name            | Species      | Age |
# |-----------------|--------------|-----|
# | Benjamin Sisko  | Human        |  40 |
# | Jadzia Dax      | Trill        | 300 |
# | Kira Nerys      | Bajoran      |  29 |
insert_query = "insert into Roster values('Benjamin Sisko', 'Human', 40), ('Jadzia Dax', 'Trill', 300), ('Kira Nerys', 'Bajoran', 29)"

cursor.execute(insert_query)



# 3. Update the Name of Jadzia Dax to be Ezri Dax
update_query = "update Roster set Name = 'Ezri Dax' where Name = 'Jadzia Dax'"

cursor.execute(update_query)


# 4.  Display the Name and Age of everyone in the table classified as Bajoran.
select_query = "select Name, Age from Roster where Species = 'Bajoran'"

data = cursor.execute(select_query)

[print(*i) for i in data]

connection.commit()

cursor.close()
connection.close()
