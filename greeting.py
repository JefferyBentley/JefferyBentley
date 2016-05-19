#greeting.py

#Write a program  that when run prompts the user for their name and age,
#then prints a greeting and a message about how old they are.

def name_age():
    name = str(input("What is your name? "))
    age = int(input("What is your age? "))

    year_from_now = (age + 1)
    print("Hi,", name, "a year form now you will be", year_from_now)

name_age()
