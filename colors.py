from colorama import init

init(autoreset=True)

# Store all of the colors for use in the game
class Colors:
    BLUE = "\033[34;49m"
    BLUE_BG = "\033[48;5;4m"
    RED = "\033[31;49m"
    GREEN = "\033[32;49m"
    YELLOW = "\033[38;5;11m"
    RESET = "\033[0m"
