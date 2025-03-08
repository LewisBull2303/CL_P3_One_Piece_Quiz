import os
import random
import time
from datetime import datetime

import gspread
import validation as val
from colors import Colors as Col
from google.oauth2.service_account import Credentials
from tabulate import tabulate

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("quiz_leaderboard")
SCOREBOARD = SHEET.worksheet("scores")
PLAYER_SHEET = SHEET.worksheet("users")

score = 0
player_score = []
today = datetime.now()
date = today.strftime("%d/%m/%y")

scoreboard_data = SCOREBOARD.get_all_values()


def ascii_logo():
    """
    This will be my function to print my logo
    """

    print(
        Col.BLUE
        + """
⠀⠀⡶⠛⠲⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡶⠚⢲⡀⠀
⣰⠛⠃⠀⢠⣏⠀⠀⠀⠀⣀⣠⣤⣤⣤⣤⣤⣤⣤⣀⡀⠀⠀⠀⣸⡇⠀⠈⠙⣧
⠸⣦⣤⣄⠀⠙⢷⣤⣶⠟⠛⢉⣁⣠⣤⣤⣤⣀⣉⠙⠻⢷⣤⡾⠋⢀⣠⣤⣴⠟
⠀⠀⠀⠈⠳⣤⡾⠋⣀⣴⣿⣿⠿⠿⠟⠛⠿⠿⣿⣿⣶⣄⠙⢿⣦⠟⠁⠀⠀⠀
⠀⠀⠀⢀⣾⠟⢀⣼⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣷⡄⠹⣷⡀⠀⠀⠀
⠀⠀⠀⣾⡏⢠⣿⣿⡯⠤⠤⠤⠒⠒⠒⠒⠒⠒⠒⠤⠤⠽⣿⣿⡆⠹⣷⡀⠀⠀
⠀⠀⢸⣟⣠⡿⠿⠟⠒⣒⣒⣈⣉⣉⣉⣉⣉⣉⣉⣁⣒⣒⡛⠻⠿⢤⣹⣇⠀⠀
⠀⠀⣾⡭⢤⣤⣠⡞⠉⠉⢀⣀⣀⠀⠀⠀⠀⢀⣀⣀⠀⠈⢹⣦⣤⡤⠴⣿⠀⠀
⠀⠀⣿⡇⢸⣿⣿⣇⠀⣼⣿⣿⣿⣷⠀⠀⣼⣿⣿⣿⣷⠀⢸⣿⣿⡇⠀⣿⠀⠀
⠀⠀⢻⡇⠸⣿⣿⣿⡄⢿⣿⣿⣿⡿⠀⠀⢿⣿⣿⣿⡿⢀⣿⣿⣿⡇⢸⣿⠀⠀
⠀⠀⠸⣿⡀⢿⣿⣿⣿⣆⠉⠛⠋⠁⢴⣶⠀⠉⠛⠉⣠⣿⣿⣿⡿⠀⣾⠇⠀⠀
⠀⠀⠀⢻⣷⡈⢻⣿⣿⣿⣿⣶⣤⣀⣈⣁⣀⡤⣴⣿⣿⣿⣿⡿⠁⣼⠟⠀⠀⠀
⠀⠀⠀⢀⣽⣷⣄⠙⢿⣿⣿⡟⢲⠧⡦⠼⠤⢷⢺⣿⣿⡿⠋⣠⣾⢿⣄⠀⠀⠀
⢰⠟⠛⠟⠁⣨⡿⢷⣤⣈⠙⢿⡙⠒⠓⠒⠓⠚⣹⠛⢉⣠⣾⠿⣧⡀⠙⠋⠙⣆
⠹⣄⡀⠀⠐⡏⠀⠀⠉⠛⠿⣶⣿⣦⣤⣤⣤⣶⣷⡾⠟⠋⠀⠀⢸⡇⠀⢠⣤⠟
⠀⠀⠳⢤⠼⠃⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠘⠷⢤⠾⠁⠀
          

"""
    )

    print("------------------------------\n")
    print("Welcome to the One Piece Quiz")


def clear_screen():
    """
    This will clear the terminal so all of the information
    on the terminal
    """
    os.system("cls" if os.name == "nt" else "clear")


def quiz_start(questions):
    """
    This function will start the quiz and start the main game loop
    """
    questions_list = random.sample(questions, 15)
    global score
    score = 0
    for question in questions_list:
        answer = input(question.cue).lower()
        if answer not in {"1", "2", "3", "4"}:
            print(Col.RED + "Wrong Answer!\n Please use 1, 2 or 3 to answer!\n")
            answer = input(question.cue).lower()

        if answer == question.answer:
            score += 1
            print(Col.GREEN + "\nCorrect!\n")
        else:
            print(Col.RED + "\nWrong Answer!\n")
    leaderboard()


def get_player_stats():
    """
    This function will gather the players stats and put them in a dictionary
    for the end of the game so it can be displayed along with the players
    score
    """
    player_stats = {"Name": val.name, "Score": str(score), "Email": val.email}

    if score >= 7:
        print(
            Col.GREEN
            + f"\nCongratulations {player_stats['Name']} you scored {player_stats['Score']} you are a true one piece fan!\n"
        )
    else:
        print(
            Col.RED
            + f"\nOh no {player_stats['Name']} only scored {player_stats['Score']} you need to go back and study!\n"
        )


def instructions():
    """
    This function will explain to the player how the game will work and how they can win
    """
    print(
        """
The quiz will ask you 15 random questions from a possible pool of 30\n
You then have to chose an answer 1, 2 or 3. All questions are multiple choice\n
The questions will be themed around the anime One Piece\n
Some questions will be easier to answer and other more difficult\n
At the end you will have the option to post your score onto the  to see how you did against
the other players
    """
    )
    input(Col.YELLOW + "Enter any key to return to the home page")
    clear_screen()
    ascii_logo()
    main_menu()


def main_menu():
    """
    This function will be the main menu for the player
    When they are done with the quiz they will be re-directed here and when they
    want to quit they can do so from here
    """
    print("Please choose an option from below:\n")
    menu_options = "1) Play\n2) Scoreboard\n3) How to play\n4) Quit\n"
    selected_option = input(menu_options)

    while selected_option not in ("1", "2", "3", "4"):
        print(Col.RED + "Please select an option either 1, 2, 3 or 4")
        selected_option = input(menu_options)

    if selected_option == "1":
        clear_screen()
        val.start_game()
        clear_screen()
        ascii_logo()
        quiz_start(questions)

    elif selected_option == "2":
        clear_screen()
        ascii_logo()
        print("\nScoreboard")
        print(tabulate(scoreboard_data))
        input(Col.YELLOW + "Press any key to return:\n")
        clear_screen()
        main_menu()

    elif selected_option == "3":
        clear_screen()
        instructions()

    elif selected_option == "4":
        clear_screen()
        print("Thanks for playing!")
        exit()


def leaderboard():
    get_player_stats()
    add_score = input(
        "Would you like to add your score to the scoreboard? Y or N\n"
    ).lower()

    while True:
        if add_score == "y":
            clear_screen()
            update_leaderboard()
            break

        elif add_score == "n":
            print(Col.BLUE + "Okay... returning to the main menu...")
            time.sleep(2)
            print_loading()
            clear_screen()
            main_menu()
            break
        else:
            print(Col.RED + "Please choose a correct option Y or N")
            add_score = input(
                "Would you like to add your score to the scoreboard? Y or N\n"
            ).lower()


def update_leaderboard():
    """
    This function will be called to add the players score
    to the leaderboard and add their stats in too
    """
    print(Col.BLUE + "\nUpdating the leaderboard...\n")
    player_score.append(val.name)
    player_score.append(score)
    player_score.append(date)
    SCOREBOARD.append_row(player_score)
    print(Col.GREEN + "\nScoreboard has now been updated!")

    input(Col.YELLOW + "Please press any key to return to the main menu: \n")
    clear_screen()
    ascii_logo()
    main_menu()


class questions_answer:
    """
    This function will get the question and check the answer for them
    """

    def __init__(self, cue, answer):
        self.cue = cue
        self.answer = answer


def print_loading():
    print("=" * 30)
    print("\nLoading...\n")
    print("=" * 30)


questions_call = [
    "What is the name of the main protagonist in One Piece?\n \
     1) Luffy\n \
     2) Zoro\n \
     3) Kaido\n ",
    "Where was Gol D. Roger born?\n \
     1) East Blue\n \
     2) West Blue\n \
     3) South Blue\n ",
    "What is the name of the village Luffy was born in?\n \
     1) Cocoyasi Village\n \
     2) Shimotsuki Village\n \
     3) Foosha Village\n ",
    "What Devil Fruit did Luffy Eat?\n \
     1) Mera Mera Fruit\n \
     2) Gum Gum Fruit\n \
     3) Yami Yami Fruit\n ",
    "What One Piece' character is a skilled swordsman who always carries three katanas with him?\n \
     1) Brook\n \
     2) Zoro\n \
     3) Sanji\n ",
    "What is the name of the strongest swordsman?\n \
     1) King\n \
     2) Marco\n \
     3) Mihawk\n ",
    "During What arc did Robin officially join the strawhats?\n \
     1) Enis Lobby\n \
     2) Water 7\n \
     3) Marineford\n ",
    "Who ate the Ice Ice Fruit?\n \
     1) Aokiji\n \
     2) Kizaru\n \
     3) Sengoku\n ",
    "What is the name of the warden at Impel Down?\n \
     1) Buggy\n \
     2) Shiryu\n \
     3) Magellan\n ",
    "What is the name of the dragon that helped the straw hats climb to Zou?\n \
     1) Nekozaemon\n \
     2) Ryunosuke\n \
     3) Kuro\n ",
    "Which of the below characters is an Admiral\n \
     1) Garp\n \
     2) Kuzan\n \
     3) Sengoku\n ",
    "What is the name of the strawhats first ship?\n \
     1) Going Merry\n \
     2) Thousand Sunny\n \
     3) Tsunami\n ",
    "What is the first Island that the straw hats visit after the time skip?\n \
     1) Dressrosa\n \
     2) Punk Hazard\n \
     3) Fish-man Island\n ",
    "What is the name of the drug Caesar created in the form of a candy?\n \
     1) SMILE\n \
     2) FUN\n \
     3) JOY\n ",
    "What is the name of the Doctor who looked after Chopper?\n \
     1) Dr Hirilk\n \
     2) Dr Crocus\n \
     3) Dr Law\n ",
    "What is the name of the mad scientist in the egghead island arc?\n \
     1) Dr Kuma\n \
     2) Dr Egghead\n \
     3) Dr Vegapunk\n ",
    "What is the name of the kingdown which is erased in chapter 1060?\n \
     1) Lulusia Kingdom\n \
     2) Kuraigana Kingdom\n \
     3) Kiseki Kingdom\n ",
    "What is the name of the island where the Revolutionary Army's base is located?\n \
    1) Momoiro Island\n \
    2) Kuraigana Island\n \
    3) Ruskaina Island\n ",
    "What is the Military rank is Kong?\n \
     1) Vice-Admiral\n \
     2) Admiral\n \
     3) Commander-in-Chief\n ",
    "What is the first name that Nico Robin is introduced as?\n \
     1) Miss All Sunday\n \
     2) Miss Wednesday\n \
     3) Miss Friday\n ",
    "Who is the only person to ever harm Luffys Straw Hat?\n \
     1) Akainu\n \
     2) Garp\n \
     3) Buggy\n ",
    "Who gave shanks his scar on his eye?\n \
     1) Whitebeard\n \
     2) Blackbeard\n \
     3) Gol. D. Roger\n ",
    "When Mr. 2 was on the Going Merry who did he not touch?\n \
     1) Chopper\n \
     2) Sanji\n \
     3) Zoro\n ",
    "How many agents of Baroque works do we see?\n \
     1) 9\n \
     2) 11\n \
     3) 13\n ",
    "What is the name of the leader of CP9\n \
     1) Rob Lucci\n \
     2) Blueno\n \
     3) Spandam\n ",
    "Which of the following pirates is NOT part of the worst generation?\n \
     1) Blackbeard\n \
     2) X Drake\n \
     3) Doflamingo\n ",
    "Who sent all of the strawhats to different islands in the sabaody archipelago arc?\n \
     1) Kuma\n \
     2) Shanks\n \
     3) Silvers Rayleigh\n ",
    "Who Stowed away in a barrel after Wano on the Thousand Sunny?\n \
     1) Kin'mon\n \
     2) Raizo\n \
     3) Caribou\n ",
    "What game is Fijitora playing when he is introduced?\n \
     1) Poker\n \
     2) Dice\n \
     3) Roulette\n ",
    "Who was able to communicate with Zunesha?\n \
     1) Gol D. Roger\n \
     2) Luffy\n \
     3) Momonosuke\n ",
]

questions = [
    questions_answer(questions_call[0], "1"),
    questions_answer(questions_call[1], "1"),
    questions_answer(questions_call[2], "3"),
    questions_answer(questions_call[3], "2"),
    questions_answer(questions_call[4], "2"),
    questions_answer(questions_call[5], "3"),
    questions_answer(questions_call[6], "1"),
    questions_answer(questions_call[7], "1"),
    questions_answer(questions_call[8], "2"),
    questions_answer(questions_call[9], "2"),
    questions_answer(questions_call[10], "2"),
    questions_answer(questions_call[11], "1"),
    questions_answer(questions_call[12], "3"),
    questions_answer(questions_call[13], "1"),
    questions_answer(questions_call[14], "1"),
    questions_answer(questions_call[15], "3"),
    questions_answer(questions_call[16], "1"),
    questions_answer(questions_call[17], "1"),
    questions_answer(questions_call[18], "3"),
    questions_answer(questions_call[19], "1"),
    questions_answer(questions_call[20], "3"),
    questions_answer(questions_call[21], "2"),
    questions_answer(questions_call[22], "2"),
    questions_answer(questions_call[23], "2"),
    questions_answer(questions_call[24], "3"),
    questions_answer(questions_call[25], "3"),
    questions_answer(questions_call[26], "1"),
    questions_answer(questions_call[27], "3"),
    questions_answer(questions_call[28], "3"),
    questions_answer(questions_call[29], "3"),
]


score = 0
clear_screen()
ascii_logo()
main_menu()
