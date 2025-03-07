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
password = ''
user_details = []

def check_user() -> str:
    """
    Checks if player has played previously,
    Calls on get email function to validate the email
    """
    print('Is this your First time here?\n')
    reply = '1) Yes \n2) No\n'
    response = input(reply).lower()

    while response not in ('1', 'y', '2', 'n'):
        print('\nPlease choose one of the below option:\n')
        response = input(reply).lower()

    if response == '1' or response == 'y':
        print('You answered yes\n')
        register_user()
        return True

    elif response == '2' or response == 'n':
        print('You answered no\n')
        player_login()
        return False

def get_email():
    """
    This function will get the players email to store in the players spreadsheet
    """
    global email
    email = input("\nWhat is your email address?:\n").lower()
    validate_user_email(email)
    return email, True

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

def get_password():
    global password

    password_prompt = ("Please enter a password: ")
    password = input(password_prompt)

    try:
        if len(password) < 7:
            raise ValueError("""
                Password needs to be at least 8 Characters long"
            """)
    except ValueError as e:
        print("Invalid Password length, Please try again.")
        get_password()
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
    print("=======================================")
    print("\nLoading...\n")
    print("=======================================")
    time.sleep(1)
    clear_screen()
    get_email()
    get_user_name()
    get_password()
    user_details.append(name)
    user_details.append(email)
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
        get_email()
        user_email = email
        existing_email = check_emails(user_email)

        if existing_email:
            player_email_row = USER_SHEET.find(user_email).row
            player_name = USER_SHEET.row_values(player_email_row)[0]

            password = USER_SHEET.row_values(player_email_row)[2]

            password_check = input("\nExisitng email was found, Please enter your password: \n")
            while True:
                if password_check == password:
                    print("Welcome back " + player_name)
                    break
                else:
                    print(password)
                    print("Incorrect password, please try again or type q to go back\n")
                    password_check = input("Please enter your password: \n")
                    if password_check.lower() == "q":
                        check_user()
                        break
                    else:
                        continue
        else:
            print("\nEmail not found in the database, re-directing you to the registration page...")
            clear_screen()
            register_user()

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