import gspread
from google.oauth2.service_account import Credentials

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
        get_email()
        print(f'\nYour email is {email}\n')
        player_login()
        return True

    elif response == '2' or response == 'n':
        print('You answered no\n')
        get_email()
        validate_user_email(email)
        get_user_name()
        return False

def get_email():
    """
    This function will get the players email to store in the players spreadsheet
    """
    global email
    email = input("What is your email address?:\n")
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

def get_user_name():
    """
    This function will scan my spreadsheet for the players email and retrieve
    their name to say hello to them
    """
    global name
    global player_name
    try:
        player_email_row = USER_SHEET.find(email).row
        player_name = USER_SHEET.row_values(player_email_row)[0]
        print(f'Welcome,\n: {player_name}\n')
        input('\nEnter any key to continue:\n')

        name = player_name
        return player_name, True

    except AttributeError:
        print('\nEmail was not found in past player records, adding now')
        player_login()

def register_user():
    """
    This function will add the new players to the spreadsheet, adding their email and
    name in order for them to be saved. This was the player can login again under the
    same details again if they play more than once
    """
    user_details.append(name)
    user_details.append(email)
    print(user_details)
    USER_SHEET.append_row(user_details)

def player_login():
    """
    This function ask the user for their name to be able to
    register them to the spreadsheet, this wat when they can
    login again in the future.
    """
    global name
    name = input('\nWhat is your name?:\n')

    try:
        if len(name) < 3 or len(name) > 12:
            raise ValueError(
                """Name needs to be at least 3 characters
                or maximum 12 characters"""
            )

    except ValueError as e:
        print(f'Invalid name length: {e},\nplease try again.\n')
        player_login()
        return False

    print(f'Welcome {name}\n')

    input('\nEnter any key to continue:\n')
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

check_user()