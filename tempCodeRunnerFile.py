
    """
    This function will be the main menu for the player
    When they are done with the quiz they will be re-directed here and when they 
    want to quit they can do so from here
    """
    print("Please choose an option from below:\n")
    menu_options = "1) Play\n2) Scoreboard\n3) How to play\n4) Quit\n"
    selected_option = input(menu_options)
    
    while selected_option not in ("1", "2", "3", "4"):
        print("Please select an option either 1, 2, 3 or 4")
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
        print("Scoreboard")
        print(tabulate(scoreboard_data))
        input("Press any key to return:\n")
        clear_screen()
        main_menu()
    
    elif selected_option == "3":
        clear_screen()
        instructions()
    
    elif selected_option == "4":
        clear_screen()