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
SHEET = GSPREAD_CLIENT.open('scoreboard')
SCOREBOARD = SHEET.worksheet('scores')
PLAYER_SHEET = SHEET.worksheet('players')

name = ''
email = ''
player_details = []

def get_emails():
    """
    This function will get the players email to store in the players spreadsheet
    """
    global email
    email = input("What is your email address?:\n")

    try:
        validate_email(email)
        return True
    except EmailNotValidError as e:
        print(str(e))
        print("Sorry this email is not valid, Please Try again!\n")
        get_emails()
        return False

def get_player_name():
    """
    This function will scan my spreadsheet for the players email and retrieve
    their name to say hello to them
    """
    global name
    global player_name
    try:
        player_email_row = PLAYER_SHEET.find(email).row
        player_name = PLAYER_SHEET.row_values(player_email_row)[0]
        print(f'Welcome,\n: {player_name}\n')
        input('\nEnter any key to continue:\n')

        name = player_name
        return player_name, True

    except AttributeError:
        print('\nEmail was not found in past player records, adding now')

def register_player():
    """
    This function will add the new players to the spreadsheet, adding their email and
    name in order for them to be saved. This was the player can login again under the
    same details again if they play more than once
    """
    player_details.append(name, email)
    PLAYER_SHEET.append_row(player_details)