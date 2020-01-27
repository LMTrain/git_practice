# Importing the `datetime` module
from datetime import datetime

# Creating a date using year, month, day as arguments.
birthday = datetime(1974, 8, 18, 12, 35, 20)
print(birthday.year)
print(birthday.month)
print(birthday.day)
print(birthday.hour)
print(birthday.weekday())

# creating a date using datetime.now()
print(datetime.now())
print(datetime.now() - datetime(2018, 1, 1))

# Parsing a date using strptime
parsed_date = datetime.strptime('Jan 15, 2018', '%b %d, %Y')
print(parsed_date.month)
print(parsed_date.year)

# Rendering a date as a string using strftime
date_string = datetime.strftime(datetime.now(), '%b %d, %Y')
print(date_string)