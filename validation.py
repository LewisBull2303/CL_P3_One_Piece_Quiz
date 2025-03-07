import gspread
from google.oauth2.service_account import Credentials
import os
import time

from email_validator import validate_email, EmailNotValidError

#  Scope and constant variables for google api and sheets
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]


#  Constants for credentials to authorise access to database
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('quiz_leaderboard')
SCOREBOARD = SHEET.worksheet('scores')
USER_SHEET = SHEET.worksheet('users')

name = ''
email = ''
user_details = []

def start_game():
    """
    This function will check if the user has played the game before
    """
    global user_details
    user_details = []
    print("Have you played before?\n")
    question = "1) Yes\n2) No\n"
    answer = input(question)

    if answer == "1" or answer == "y":
        player_login()
    elif answer == "2" or answer == "n":
        register_user()
    
    return answer

def get_email() -> str:
    """
    This function will just get the users email
    """
    global email
    while True:
        email = input("What is your email address?\n")

        if validate_user_email(email):
            break

    return email

def validate_user_email(email: str):
    """
    This functions validates the users email to be able to have a chain
    of functions when registering the user
    The emails must be in the format -> something@somthing.com
    """
    try:
        validate_email(email)
        return True
    except EmailNotValidError as e:
        print(str(e))
        print("Sorry this email is not valid, Please Try again!\n")
        get_email()
        return False

def get_user_name():
    """
    This function will scan my spreadsheet for the players email and retrieve
    their name to say hello to them
    """
    global name
    name = input("\nWhat is your name?: \n")
    return name, True

def register_user():
    """
    This function will add the new players to the spreadsheet, adding their email and
    name in order for them to be saved. This was the player can login again under the
    same details again if they play more than once
    """
    print("Creating a new user...")
    print_loading()
    create_new_user()
    
    update_user_worksheet()
    
def create_new_user() -> list:
    """
    Creates the new user
    Gets the players name and email
    Checks if the information is already in the database
    """
    global email
    global name
    global user_details
    email_column = USER_SHEET.col_values(2)
    print(email_column)

    while True:
        name = input("What is your name: \n")
        user_details.append(name)
        break

    while True:
        user_email = get_email()

        if user_email not in email_column:
            print("Thank you!")
            user_details.append(email)
            break

        else:
            print(f"Sorry {name}, this email is already used.")
            print("Please try another email")
    return [name, email]

def update_user_worksheet():
    USER_SHEET.append_row(user_details)

def player_login():
    """
    This function ask the user for their name to be able to
    register them to the spreadsheet, this wat when they can
    login again in the future.
    """
    global password
    global email
    while True:
        user_email = email
        existing_email = check_emails(user_email)

        if existing_email:
            player_email_row = USER_SHEET.find(user_email).row
            player_name = USER_SHEET.row_values(player_email_row)[0]

            print("Welcome", player_name + "!")
            break
        else:
            input_correct_email()
            break

def input_correct_email():
    """
    Asks players to input their email
    again if the email was not found in the datebase
    """
    print("Sorry this email is not registered\n")
    email_option = email_not_registered()

    if email_option == "1":
        print("Please write your email again:")
    elif email_option == "2":
        register_user()

def email_not_registered() -> str:
    """
    Called when the users email is not registered on the database
    Give the user an option to enter another email or create a new user
    """
    print("Would you like to: ")
    options = "1) Try another email\n2) Create a new account\n"
    email_option = input(options)

    while email_option not in ("1", "2"):
        print("Please choose between one of the option:")
        email_option = input(options)
    return email_option

def total_scores():
    """
    this function will calculate the total score of all players 
    """
    score_column = SCOREBOARD.col_values(2)
    total_score = 0

    del score_column[0]
    score_column = list(map(int, score_column))

    for i in score_column:
        total_score += i

    return total_score

def check_emails(email : str) -> bool:
    """
    This function will check if the user has previously logged in and
    didnt remember, it will loop through all of the emails and check if the email has
    already been registered
    """
    email_column = USER_SHEET.col_values(2)

    if email in email_column:
        return True
    else:
        return False

def clear_screen():
    """
    This will clear the terminal so all of the information
    on the terminal
    """
    os.system("cls" if os.name == "nt" else "clear")

def print_loading():
    print("=======================================")
    print("\nLoading...\n")
    print("=======================================")
