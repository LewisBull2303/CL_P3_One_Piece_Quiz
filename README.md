# ONE PIECE QUIZ GAME
## Developer: Lewis Bull

## About
This is a command-line version of a One Piece-themed quiz game for a single player.

In this quiz game, the player answers a series of multiple-choice questions based on the world of One Piece. The questions cover characters, story arcs, and various other aspects of the One Piece universe.

The objective of the game is to answer as many questions correctly as possible. Each correct answer earns points, and the game ends when all questions have been answered or the player decides to quit. Test your knowledge of One Piece and see how well you know the world.

## Project Goals

### User Goals

Play a fun and engaging game by answering One Piece trivia
Read and understand the rules of the quiz game
Track progress and score throughout the game

### Site Owner Goals

Create a game that is easy to play and clear to the user
Ensure that players understand the objective of the quiz game
Provide feedback to the player during gameplay (e.g., correct/incorrect answers, score updates)
Offer an enjoyable and interactive experience for One Piece fans

## User Experience

### Target Audience
The target audience of this game is One Piece fans of all ages. This is because the trivia is all based around One Piece and 

### User Requirements and Expectations

A simple, fun and error-free game experience
Easy and intuitive navigation through the quiz
The ability to personalize the game by entering the player's name
Clear feedback on game results (e.g., correct/incorrect answers, final score)

## User Stories

### Users
1. As a user, I want to have clear options in the main menu
2. As a user, I want to be able to read the rules and have instructions for the game
3. As a user, I want to be able to enter my name
4. As a user, I want to be able to enter my email
5. As a user, I want the game to catch if I enter my email after I already registered
6. As a user, I want feedback throughout the game
7. As a user, I want to know my score
8. As a user, I want to be able to play multiple times after logging in
9. As a user, I want to see a scoreboard of all the best players
10. As a user, I want to be able to login if I return

### Site Owner 
11. As a site owner, I want user to have feedback from the game in real-time 
12. As a site owner, I want my UI to be obvious and easy to navigate for my users
13. As a site owner, I want the users names and emails to be saved in a google spreadsheet
14. As a site owner, I want the user to know if there was a wrong input
15. As a site owner, I want the users data to be validated to check if its correct
16. As a site owner, I want the user to be able to choose if they want to upload their score
17. As a site owner, I want the user to be able to login after closing the game

## Technical Design

Flowcharts:
<details>
 <summary>Flowcharts</summary>

![image](https://github.com/user-attachments/assets/89742f06-f318-46de-896e-c9b31525fcc6)

![image](https://github.com/user-attachments/assets/ec256342-0840-4aad-b63f-d19cf4783580)

</details>
</br>

## Technologies Used

### Languages
- Python - programming language for the logic of the project, where the majority of the project is.

### Frameworks & Tools
- [Miro](https://miro.com/) was used to draw program flowchart
- [Git](https://git-scm.com/) was used for version control within VSCode to push the code to GitHub
- [GitHub](https://github.com/) was used as a remote repository to store project code
- [Google Cloud Platform](https://cloud.google.com/) was used to manage access and permissions to the Google Services such as Google auth, sheets etc.
- [Google Sheets](https://docs.google.com/spreadsheets/u/0/) was used to store users details
- [Heroku](https://www.heroku.com/) was used to load the project on to a website and hosting the website
- [Visual Studio Code](https://code.visualstudio.com/) VSCode was used to write the project code

  
### Third Party Libraries
- [Colorama](https://pypi.org/project/colorama/) - Colorama was used to add color and more life to my game which will make it more interesting and engaging to the user
- [Email_Validator](https://pypi.org/project/email-validator/) - I used this to check if the user is entering a valid email and if not to bring up an error
- [Gspread](https://docs.gspread.org/_/downloads/en/v5.6.0/pdf/) - This was used to append rows to the database which is a google spreadsheet. It was also used to fetch existing information from the database
- [Google.Oauth2.service_account](https://google-auth.readthedocs.io/en/master/) -  Module used to set up the authentication between the database and the user. It was needed in order to store data. A creds.json file was created with all of the details the API needs and was passed into the configs in heroku
