#Write a Python program to create a person class. Include attributes like name,country and date of birth. Implement a method to determine the person's age.


from datetime import date

name = input("Enter your name: ")
country = input("Enter your country: ")
year = int(input("Enter your year of birth: "))
month = int(input("Enter your month of birth (Enter as an integer, e.g., 'jan'='1'): "))
date_birth = int(input("Enter your date of birth: "))
birthdate = date(year, month, date_birth)
today = date.today()
age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
print(name," is",age," years old.")