import gspread
from google.oauth2.service_account import Credentials
import os
import time
from colors import Colors as Col
from email_validator import validate_email, EmailNotValidError

# Scope and constant variables for Google API and sheets
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

# Constants for credentials to authorize access to the database
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('quiz_leaderboard')
SCOREBOARD = SHEET.worksheet('scores')
USER_SHEET = SHEET.worksheet('users')

# Global variables to store user information
name = ''
email = ''
user_details = []


def start_game():
    """
    Handles the game start by checking if the user has played before.
    It will direct the user to either login or register based on their response.
    """
    global user_details
    user_details = []
    print("Have you played before?\n")
    question = "1) Yes\n2) No\n"
    answer = input(question)

    # Loop to validate user input
    while True:
        if answer == "1" or answer.lower() == "y":
            player_login()
            break
        elif answer == "2" or answer.lower() == "n":
            register_user()
            break
        else:
            print(Col.RED + "Please choose either 1 or 2")
            answer = input(question)

    return answer


def get_email() -> str:
    """
    Prompts the user to enter their email address and validates it.
    If the email is valid, it proceeds; otherwise, it prompts again.
    """
    global email
    while True:
        email = input("\nWhat is your email address?\n").lower()
        clear_screen()
        print_loading()
        time.sleep(2)
        clear_screen()
        if validate_user_email(email):
            break

    return email


def validate_user_email(email: str):
    """
    Validates the user's email format using the email_validator package.
    Returns True if valid, otherwise prompts the user to try again.
    """
    try:
        validate_email(email)
        print("=" * 30)
        print("\nEmail Validated!\n")
        print("=" * 30)
        return True
    except EmailNotValidError as e:
        print(str(e))
        print(Col.RED + "Sorry, this email is not valid. Please try again!\n")
        get_email()
        return False


def get_user_name():
    """
    Prompts the user to enter their name.
    This is mainly used when registering a new user.
    """
    global name
    name = input("\nWhat is your name?: \n")
    return name, True


def register_user():
    """
    Handles the registration of a new user.
    It collects the user's name and email, then updates the spreadsheet.
    """
    print("\nCreating a new user...")
    print_loading()
    create_new_user()

    # Check if the email is already registered
    if email not in USER_SHEET.col_values(2):
        update_user_worksheet()


def create_new_user() -> list:
    """
    Gathers the user's name and email to create a new user entry.
    Also checks if the email already exists to avoid duplicates.
    """
    global email
    global name
    global user_details
    email_column = USER_SHEET.col_values(2)

    # Collect the user's name
    while True:
        name = input("\nWhat is your name: \n")
        user_details.append(name)
        time.sleep(2)
        break

    # Collect the user's email
    while True:
        user_email = get_email()

        # If email is not registered, add the user
        if user_email not in email_column:
            print(Col.GREEN + "Thank you!")
            print(f"\nWelcome {name}")
            time.sleep(1)
            print_loading()
            time.sleep(2)
            clear_screen()
            user_details.append(email.lower())
            break
        else:
            # If email already exists, give options
            print(Col.RED + f"Sorry {name}, this email is already used.\n")
            print("Would you like to: \n")
            options = f"""1) Try another email\n
2) Login with this email {email}\n"""
            answer = input(options)

            # Validate input
            while answer not in ("1", "2"):
                print(Col.RED + "Please choose either 1 or 2")
                answer = input(options)

            if answer == "1":
                clear_screen()
                print_loading()
                time.sleep(2)
                continue
            elif answer == "2":
                clear_screen()
                print_loading()
                time.sleep(2)
                player_login()
                break

    return [name, email.lower()]


def update_user_worksheet():
    """
    Updates the user worksheet with the new user's details.
    """
    USER_SHEET.append_row(user_details)


def player_login():
    """
    Handles user login by verifying if the email exists in the database.
    If the email is found, the user is welcomed back; otherwise, prompted to re-enter.
    """
    global name
    global email
    while True:
        if email == "":
            user_email = get_email()
        else:
            user_email = email.lower()

        # Check if the email exists
        existing_email = check_emails(user_email.lower())

        if existing_email:
            player_email_row = USER_SHEET.find(user_email).row
            name = USER_SHEET.row_values(player_email_row)[0]
            clear_screen()
            print(Col.GREEN + "Welcome back", name + "!")
            time.sleep(2)
            print_loading()
            time.sleep(3)
            clear_screen()
            break
        else:
            input_correct_email()
            break


def input_correct_email():
    """
    Handles invalid email input during login.
    Prompts the user to either re-enter their email or register as a new user.
    """
    print(Col.RED + "Sorry, this email is not registered\n")
    email_option = email_not_registered()

    if email_option == "1":
        print("Please write your email again:")
    elif email_option == "2":
        print_loading()
        time.sleep(2)
        register_user()


def email_not_registered() -> str:
    """
    Provides options for the user when their email is not found in the database.
    They can either enter another email or create a new account.
    """
    print("Would you like to: ")
    options = "1) Try another email\n2) Create a new account\n"
    email_option = input(options)

    # Ensure the user enters a valid option
    while email_option not in ("1", "2"):
        print(Col.RED + "Please choose between one of the options:")
        email_option = input(options)
    return email_option


def total_scores():
    """
    Calculates the total scores of all players from the spreadsheet.
    This is useful for leaderboard statistics.
    """
    score_column = SCOREBOARD.col_values(2)
    total_score = 0

    # Remove the header from the column
    del score_column[0]
    score_column = list(map(int, score_column))

    # Calculate total score
    for i in score_column:
        total_score += i

    return total_score


def check_emails(email: str) -> bool:
    """
    Checks if an email exists in the database.
    Returns True if found, False otherwise.
    """
    email_column = USER_SHEET.col_values(2)

    if email in email_column:
        return True
    else:
        return False


def clear_screen():
    """
    Clears the terminal screen to make the output cleaner.
    Compatible with Windows, Linux, and MacOS.
    """
    os.system("cls" if os.name == "nt" else "clear")


def print_loading():
    """
    Simulates a loading effect with a simple message.
    """
    print("=" * 30)
    print("\nLoading...\n")
    print("=" * 30)
