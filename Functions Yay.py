# Functions Yay
# Brayden Towner
# 11/09/2023

import os
exercise_int=1

# Just to keep it in one file, I'll use headers and cls to clarify exercises.
# This code repeats a lot
def next_exercise(exercise_name: str):
    # It tries to grab the local variable with this name which doesn't exist...
    # I knew of this keyword already
    global exercise_int
    # Only pause pre-exercise if this isn't the first
    if exercise_int > 1:
        os.system("pause")
    os.system("cls")
    print(f"Exercise {exercise_int}: {exercise_name}\n")
    exercise_int+=1

def hello_world():
    """Prints Hello world
        no params
        no return
    """
    print("Hello world!")

def favorite_book(title):
    """Prints friendly message to people looking for books

    Args:
        title (string): The title of your favorite book
    no return
    """
    print(f"{title.title()} is probably not in stock. Leave. :)")

def square(number):
    """Squares a number

    Args:
        number (float): The number to square

    Returns:
        float: The number input squared
    """
    return number**2

def phone_number(number):
    """Prints a nice friendly message to users

    Args:
        number (int): The phone number of the user
    no return
    """
    num_as_string = str(number)
    # Basic checks to see if it's 7 or 10 digits
    if len(num_as_string) == 7:
        print(f"Thank you for submitting {num_as_string[:3]}-{num_as_string[3:]} as your phone number! We are NOT selling them to spam call companies as we speak!")
    if len(num_as_string) == 10:
        print(f"Thank you for submitting ({num_as_string[:3]}) {num_as_string[3:6]}-{num_as_string[6:]} as your phone number! We are NOT selling them to spam call companies as we speak!")
        

next_exercise("Hello world!")

hello_world()

next_exercise("I didn't want to be a librarian")

favorite_book(input("What's your favorite book? >  "))

next_exercise("Squares (How original)")

print(f"That squared is {square(float(input('What number do you want to square? >  ')))}")

next_exercise("You used to call me on my cellphone")

phone_number(1234567)
phone_number(1234567890)
