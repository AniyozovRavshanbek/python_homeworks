# 1. Task: JSON Parsing
# - write a Python script that reads the students.jon JSON file and prints details of each student.
import json

with open('14-lesson\students.json') as f:
    student_details = json.load(f)

    for student in student_details['Students']:
        print(student)


# 2. Task: Weather API
#    1. Use this url : https://openweathermap.org/
#    2. Use the requests library to fetch weather data for a specific city(ex. your hometown: Tashkent) and print relevant information (temperature, humidity, etc.).
import requests
api_key = '171ae9522e85c1d7da3e9aedecd99322'
base_url = 'http://api.openweathermap.org/data/2.5/forecast'

city = input('Enter your city(e.g Tashkent): ')

params = {
    'q': city,
    'appid': api_key,
    'units': 'metric'
}

response = requests.get(base_url, params=params)
data = response.json()

if response.status_code == 200:
    print("City:", city)
    print("Temperature:", data['list'][0]['main']['temp'], "°C")
    print("Weather:", data['list'][0]['weather'][0]['description'])
    print("Humidity:", data['list'][0]['main']['humidity'], "%")
    print("Wind speed:", data['list'][0]['wind']['speed'], "m/s")
else:
    print('Please check value')



# 3. Task: JSON Modification
#    1. Write a program that allows users to add new books, update existing book information, and delete books from the books.json JSON file
from json import load, dump

#load books
with open('14-lesson/books.json') as f:
    books = load(f)
  

#save books
def save_books(books):
    with open('14-lesson/books.json', 'w') as f:
        dump(books, f, indent=4)



#add books
def add_book(books):
    
    title = input('Enter book title: ')
    description = input('Enter book description: ')
    author = input('Enter book author(s): ')
    year = int(input('Enter released date of the book: '))

    book_details = {
        'title':title,
        'description':description,
        'author':author,
        'year':year,
    }

    books.append(book_details)

    save_books(books)
    print(f'{title} was successfully added!')


#update books
def update_book(books):
    title = input('Enter book title: ')

    for book in books:
        if book['title'] == title:
            book['title'] = input('Update title or leave the blank: ')
            book['description'] = input('Update description or leave the blank: ')
            book['author'] = input('Update author(s) name or leave the blank: ')
            book['year'] = int(input('Update year or leave the blank: '))

            print(f'{title} was successfully updated!')
        else:
            print('Please sure wheter title is correct')
    
    save_books(books)   
    print(f'{title} was successfully updated!')    
    


#delete books
def delete_book(books):
    title = input('Enter book title to delete: ')

    for i in range(len(books)):
        if books[i]['title'] == title:
            del books[i]
            print(f'{title} was successfully deleted!')
            break

        else:
            print('Please sure wheter title is correct')
    
    save_books(books)
    

#menu
def menu():
    while True:
        print('Choose option:\n')
        print('1. See book')
        print('2. Add book')
        print('3. Update book')
        print('4. Delete book')
        print('5. Exit')

        option = int(input('Please select one option above: '))

        if option == 1:
            if not books:
                print('There is no book in the list')
            else:
                for book in books:
                    print(f"Title: {book['title']}, Description: {book['description']}, Author(s): {book['author']}, Year: {book['year']}")
        elif option == 2:
            add_book(books)
        elif option == 3:
            update_book(books)
        elif option == 4:
            delete_book(books)
        elif option == 5:
            exit()
        else:
            print('Please choose correct option!')
        print()

menu()



# 4. Task: Movie Recommendation System
#    1. Use this url http://www.omdbapi.com/ to fetch information about movies.
#    2. Create a program that asks users for a movie genre and recommends a random movie from that genre.

#I used https://api.themoviedb.org, because on the http://www.omdbapi.com/, there isn't chance to search by genre
import requests
import random

genre = input('Input film genre(e.g Action, Animation): ').capitalize()

api_key = 'b2269e20b3048a43cf0a14c1b90232c5'
base_url = f'https://api.themoviedb.org/3/discover/movie'

genre_map = {
    "Action": 28,
    "Adventure": 12,
    "Animation": 16,
    "Comedy": 35,
    "Crime": 80,
    "Documentary": 99,
    "Drama": 18,
    "Family": 10751,
    "Fantasy": 14,
    "History": 36,
    "Horror": 27,
    "Music": 10402,
    "Mystery": 9648,
    "Romance": 10749,
    "Science Fiction": 878,
    "TV Movie": 10770,
    "Thriller": 53,
    "War": 10752,
    "Western": 37
}

params = {
    'api_key':api_key,
    'with_genres':genre_map.get(genre),
    'page':1

}
params['page'] = random.randint(1, 500)

response = requests.get(base_url, params=params)
data = response.json()


if genre in genre_map:
    i = random.randint(0, len(data['results'])-1)
    print('Recommended movie for you! Watch and enjoy...\n')
    print('Title:', data['results'][i]['original_title'])
    print('Description:', data['results'][i]['overview'])
    print('Released date:',data['results'][i]['release_date'])
    print('Average vote:',data['results'][i]['vote_average'])
    print('Language:', data['results'][i]['original_language'])

else:
    print('Please enter correct genre name')
