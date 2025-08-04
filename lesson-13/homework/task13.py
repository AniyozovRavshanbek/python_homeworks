# Homework:
# 1. Age Calculator: Ask the user to enter their birthdate. Calculate and print their age in years, months, and days.

from datetime import datetime, timedelta
import time
import re
import pytz

birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
today = datetime.today()

age_years = today.year - birthdate.year
age_months = today.month - birthdate.month
age_days = today.day - birthdate.day

if age_days < 0:
    age_months -= 1
    age_days += (today.replace(day=1) - timedelta(days=1)).day

if age_months < 0:
    age_years -= 1
    age_months += 12

print(f"You are {age_years} years, {age_months} months, and {age_days} days old.")


# 2. Days Until Next Birthday: Similar to the first exercise, but this time, calculate and print the number of days remaining until the user's next birthday.

birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
today = datetime.today()

next_birthday = birthdate.replace(year=today.year)
if next_birthday < today:
    next_birthday = next_birthday.replace(year=today.year + 1)

days_remaining = (next_birthday - today).days
print(f"There are {days_remaining} days until your next birthday.")


# 3. Meeting Scheduler: Ask the user to enter the current date and time, as well as the duration of a meeting in hours and minutes. Calculate and print the date and time when the meeting will end.

current_time = input("Enter the current date and time (YYYY-MM-DD HH:MM): ")
duration_hours = int(input("Enter meeting duration (hours): "))
duration_minutes = int(input("Enter meeting duration (minutes): "))

current_time = datetime.strptime(current_time, "%Y-%m-%d %H:%M")
end_time = current_time + timedelta(hours=duration_hours, minutes=duration_minutes)

print("The meeting will end at:", end_time.strftime("%Y-%m-%d %H:%M"))


# 4. Timezone Converter: Create a program that allows the user to enter a date and time along with their current timezone, and then convert and print the date and time in another timezone of their choice.

date_time_str = input("Enter date and time (YYYY-MM-DD HH:MM): ")
from_zone = input("Enter your current timezone (e.g., 'US/Eastern'): ")
to_zone = input("Enter the target timezone (e.g., 'Europe/London'): ")

dt = datetime.strptime(date_time_str, "%Y-%m-%d %H:%M")
from_tz = pytz.timezone(from_zone)
to_tz = pytz.timezone(to_zone)

localized_dt = from_tz.localize(dt)
converted_dt = localized_dt.astimezone(to_tz)

print("Converted time:", converted_dt.strftime("%Y-%m-%d %H:%M"))


# 5. Countdown Timer: Implement a countdown timer. Ask the user to input a future date and time, and then continuously print the time remaining until that point in regular intervals (e.g., every second).

future_time_str = input("Enter a future date and time (YYYY-MM-DD HH:MM:SS): ")
future_time = datetime.strptime(future_time_str, "%Y-%m-%d %H:%M:%S")

while True:
    now = datetime.now()
    remaining = future_time - now
    if remaining.total_seconds() <= 0:
        print("Countdown complete!")
        break
    print("Time remaining:", remaining)
    time.sleep(1)


# 6. Email Validator: Write a program that validates email addresses. Ask the user to input an email address, and check if it follows a valid email format.

email = input("Enter an email address: ")
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

if re.match(pattern, email):
    print("Valid email address.")
else:
    print("Invalid email address.")


# 7. Phone Number Formatter: Create a program that takes a phone number as input and formats it according to a standard format. For example, convert "1234567890" to "(123) 456-7890".

phone = input("Enter a 10-digit phone number: ")

if len(phone) == 10 and phone.isdigit():
    formatted = f"({phone[:3]}) {phone[3:6]}-{phone[6:]}"
    print("Formatted phone number:", formatted)
else:
    print("Invalid phone number.")


# 8. Password Strength Checker: Implement a password strength checker. Ask the user to input a password and check if it meets certain criteria (e.g., minimum length, contains at least one uppercase letter, one lowercase letter, and one digit).

password = input("Enter a password: ")
criteria = [
    (len(password) >= 8, "At least 8 characters"),
    (re.search(r'[A-Z]', password), "At least one uppercase letter"),
    (re.search(r'[a-z]', password), "At least one lowercase letter"),
    (re.search(r'\d', password), "At least one digit")
]

strength = all(cond for cond, _ in criteria)

if strength:
    print("Password is strong.")
else:
    print("Password is weak. Missing:")
    for cond, msg in criteria:
        if not cond:
            print("-", msg)


# 9. Word Finder: Develop a program that finds all occurrences of a specific word in a given text. Ask the user to input a word, and then search for and print all occurrences of that word in a sample text.

text = "This is a sample text where the word 'sample' appears multiple times. Sample text is simple."
word = input("Enter the word to search for: ").lower()

words = text.lower().split()
positions = [i for i, w in enumerate(words) if w.strip(".,'\"") == word]

print(f"The word '{word}' was found {len(positions)} times at positions {positions}")


# 10. Date Extractor: Write a program that extracts dates from a given text. Ask the user to input a text, and then identify and print all the dates present in the text.

text = input("Enter text containing dates: ")
pattern = r'\b\d{4}-\d{2}-\d{2}\b|\b\d{2}/\d{2}/\d{4}\b'
dates = re.findall(pattern, text)

if dates:
    print("Dates found:", dates)
else:
    print("No dates found.")
