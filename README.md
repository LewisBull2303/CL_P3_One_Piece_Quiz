# ONE PIECE QUIZ GAME
## Developer: Lewis Bull

[Live Website Link](https://clp3onepiecequiz-fb7dc9e72670.herokuapp.com/)

![image](https://github.com/user-attachments/assets/b78d9940-96a3-4277-a735-b7ad8acd5814)

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
18. As a site owner, I want the user to be welcomed to the game

## Technical Design

### Flowcharts:
<details>
 <summary>Flowcharts</summary>

![image](https://github.com/user-attachments/assets/89742f06-f318-46de-896e-c9b31525fcc6)

![image](https://github.com/user-attachments/assets/ec256342-0840-4aad-b63f-d19cf4783580)

</details>
</br>

## User Guide:
<details>
 <summary>See the user manual here</summary>
 
### Main Menu
When launching the game, users are greeted with a main menu featuring an ASCII art rendering of the jolly rodger of the Strawhat Pirates. Below this graphic, several options are provided.

Operation: Input a numeric value and press the enter key to select an option.

Play Game
View Scoreboard
View Game Rules
Quit

At any point, if a user enters a number that doesn't correspond to a valid option, they will be prompted to try again.

### Play Game
When choosing the “Play Game” option, users are asked if they have played the game before.

Yes (1)
No (2)
If "Yes" (1) is selected
If the user has played the game before, they will be prompted to log in using their email address if they have already registered.

Player is asked for their email address.
The system checks whether the email is registered.
If the email is not found
Players can choose one of the following options:

Try another email (1)
Create a new user (2)
The user can continue to try different emails until they are matched with an existing one. Once a correct email is entered, a personalized greeting is displayed with the player’s name.

If "No" (2) is selected
If the user has never played before, they are given the option to create a new account.

The following steps are required for both players:

Enter their name.
Provide an email address.
Email validation:

Email must be valid, containing exactly one "@" symbol and have a .com or .co.uk otherwise it will fail validation, (e.g., example@domain.com).
The email address must not already exist in the database.

### Game Start
Once the player has logged in, the system greets them by name and the game begins.

### Quiz
Once the game starts the user will bew given 15 multiple choice questions all around the world of one piece, it will cover the story arcs, characters and lore of the one piece universe. Once the player has answered all of the questions the game will ask them if they want to submit their score to the scoreboard.

### Scoreboard/Game Over:
When the game ends the player can select if they want to add their score to the scoreboard the options are:
1) Yes
  If yes is chosen then the players name, score and the date they played will be uploaded to the scoreboard and sorted in the scoreboard for the highest score.
2) No
If no is chosen the player will be able to press any key and be returned to the main menu where they can play again if they want.

### Go to Main Menu
This option brings players back to the main menu of the program, where they can choose to view the rules, play another game, or quit.

### Game Rules
In this section, players can review the game rules. After reading, they can return to the main menu.

Operation: Press any key and then enter to go back to the main menu.

Operation: Input a numeric value and press enter key.

### See the scoreboard:
Selecting this option displays all of the players that have played before and that have completed the game and uploaded their score to the scoreboard

### Quit Game
When choosing to quit, the user exits the program with a goodbye message.

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

### Python Libararies
- OS - Used to clear the terminal so it is less clogged and better looking
- random - Used to randomly select which questions will be asked to the user so each time the quiz is different
- time - Used to get the date to be stored in the scoreboard
  
### Third Party Libraries
- [Colorama](https://pypi.org/project/colorama/) - Colorama was used to add color and more life to my game which will make it more interesting and engaging to the user
- [Email_Validator](https://pypi.org/project/email-validator/) - I used this to check if the user is entering a valid email and if not to bring up an error
- [Gspread](https://docs.gspread.org/_/downloads/en/v5.6.0/pdf/) - This was used to append rows to the database which is a google spreadsheet. It was also used to fetch existing information from the database
- [Google.Oauth2.service_account](https://google-auth.readthedocs.io/en/master/) -  Module used to set up the authentication between the database and the user. It was needed in order to store data. A creds.json file was created with all of the details the API needs and was passed into the configs in heroku
- Tabultate - This was used to print our the scoreboard in an easy manner that looks good to the user.

## Features

### Main Menu
- Gives the user 4 options to choose from when they first load up the game.
- Gives the user a welcom message and shows off the ASCII Logo.
- Gives the user the autonomy on what they what they want to do.
- User Stories Answered:1

### Game Rule/Instructions
- Clearly shows the rules of the game and how to play.
- Allows the user to return when they type any key.
- User Stories Answered: 1, 2

### Scoreboard
- Clearly shows all of the users who have passed the game before and their scores
- Updates the scoreboard based on the highest score
- User Stories Answered: 7, 9

### Play Game
- When the user starts the game they are asked if they have played the game before.
- The user can select yes or no and each option takes the user to a different part of the validation.
- User Stories Answered: 1, 8, 10

### Login
- If the user says they have played before they are taken to the login part of the validation.
- The user is prompted to enter their email.
- If the email is not found in the database, they will be prompted to use a different email or to create a new account.
- If the email is found already registered, I will log the user in and display a welcome message with the users name.
- User Stories Answered: 3, 4, 5, 10, 13, 15, 17

### Register a New User
- If the user says they have not played before they will be taken to the register part of the validation.
- The user will be prompted to enter their name.
- The user will then be prompted to enter their email.
- The users email will be validated to make sure that it has an @ sign and a . in it.
- User Stories Answered: 3, 4, 5, 

### User Greeting
- Once the user has logged in they will be displayed a welcom message with their name.
- User Stories Answered: 18

### Main Game:
- The main part of the game is answering the quiz questions.
- Once the user has logged in/registered, the game will start.
- The user will be asked 15 out of 30 questions randomly selected, and the player will need to answer all of them.
- The users score will be calculated based on how many answers they got correct.
- After it is complete the user will be given the option to add their score to the scoreboard.
- User Stories Answered: 1, 6, 7, 11, 12, 14, 16

### Add Score to Scoreboard
- When the user is finished playing the game, a custom message will be displayed depending on their score.
- If the player scores below half the total points it will tell them that they need to study more.
- If the player scores more than half the available points the game will congratulate them.
- The user is then asked if they want to add their score to the scoreboard.
- If the user chooses no, then nothing will happen and the user will be prompted to press any key to return to the main menu.
- If the user chooses yes then their score will be added to the score board and then the user will be prompted to press any key to return to the main menu.
- User Stories Answered: 7, 16

### Quit game
- On the main menu the user can choose to quit the game which will display a goodbye message.
- User Stories Answered: 12

## Testing

### Manual Testing

1. As a user, I want to have clear options in the main menu

|Feature|Action|Expected Result|Outcome|
|---|---|---|---|
|Main Menu|Option 1 - Play Game| Users are asked if they have played the game before|Works as expected|
|Main Menu|Option 2 - How to play| Users are presented with the game instructions and how to play|Works as expected|
|Main Menu|Option 3 - Scoreboard|Users are presented with the scoreboard|Works as expected|
|Main Menu|Option 4 - Quit|The teminal quits and stops the game, and a message saying thank you for playing pops up|Works as expected|

<details>
 <summary>Images</summary>

![image](https://github.com/user-attachments/assets/4d8748ae-1cb0-4d41-b450-eebff03972dd)
![image](https://github.com/user-attachments/assets/b413da7f-69f5-4391-a304-a4e330c3ca45)
![image](https://github.com/user-attachments/assets/71590224-f065-433c-861d-935d9029c5f0)
![image](https://github.com/user-attachments/assets/7c60c3a1-a145-4d24-ad0a-80f0099027ef)
![image](https://github.com/user-attachments/assets/2f4151f1-59c4-41ed-bbd6-8a93c023f6b6)

</details>
</br>

2. As a user, I want to be able to read the rules and have instructions for the game

|Feature|Action|Expected Result|Outcome|
|---|---|---|---|
|Main Menu|Option 2 - How to play| Users are presented with the game instructions and how to play|Works as expected|
|Game Rule/Instructions|How to play option on the scoreboard| Users are presented with the game instructions and how to play|Works as expected|

<details>
 <summary>Images</summary>

![image](https://github.com/user-attachments/assets/7c60c3a1-a145-4d24-ad0a-80f0099027ef)

</details>
</br>


3. As a user, I want to be able to enter my name

|Feature|Action|Expected Result|Outcome|
|---|---|---|---|
|Login|Saved Name in the database|When the user registers they are asked for their name. When they login the database fetches the name and prints it back to the user with a welcome message|Works as expected|
|Register|Prompt the user for their name|When the user registers they are asked for their name. It then gets saved to the database|Works as expected|

<details>
 <summary>Images</summary>

![image](https://github.com/user-attachments/assets/3bb309a1-e3b6-431f-8a32-d2c24c8787e8)
![image](https://github.com/user-attachments/assets/956479c2-782d-44a9-ba50-42553119f796)
![image](https://github.com/user-attachments/assets/77456edb-5ef7-4605-904f-42b45beb4793)

</details>
</br>

4. As a user, I want to be able to enter my email

|Feature|Action|Expected Result|Outcome|
|---|---|---|---|
|Login|Prompt the user for their email|When the user logs in they are asked for their email to confirm that they have played before|Works as expected|
|Register|Prompt the user for their email|When the user registers they are asked for their email. It then gets saved to the database|Works as expected|

<details>
 <summary>Images</summary>

![image](https://github.com/user-attachments/assets/21e13861-4e0c-42ab-a927-6e123515fa47)
![image](https://github.com/user-attachments/assets/5b5d5b21-2990-4c7e-92b9-7da453b74ca0)

</details>
</br>

5. As a user, I want the game to catch if I enter my email after I already registered

|Feature|Action|Expected Result|Outcome|
|---|---|---|---|
|Login|Prompt the user for their email|When the user logs in if their email is already registered it will send a welcome message|Works as expected|
|Register|Prompt the user for their email|When the user registers they are asked for their email. If the email already exists it will notify the player|Works as expected|

<details>
 <summary>Images</summary>

![image](https://github.com/user-attachments/assets/956479c2-782d-44a9-ba50-42553119f796)
![image](https://github.com/user-attachments/assets/894d64a7-3a5b-4891-8ed8-4a162064accd)

</details>
</br>

6. As a user, I want feedback throughout the game

|Feature|Action|Expected Result|Outcome|
|---|---|---|---|
|Feedback throughout the game|Players are informed of incorrect inputs|When the user inputs and incorrect option they are informed until the input is valid|Works as expected|
|Feedback throughout the validation|Players are informed of incorrect inputs|When the user inputs incorrect information they are informed and validation will only continue when the input is correct|Works as expected|

<details>
 <summary>Images</summary>

![image](https://github.com/user-attachments/assets/7bcd358e-8eec-4c9d-b77c-8d08883ff3bd)
![image](https://github.com/user-attachments/assets/8909a981-ecd0-4ccb-85e2-a0e725d8ac6d)
![image](https://github.com/user-attachments/assets/0faf713e-2f53-40db-a9ed-785a89263399)
![image](https://github.com/user-attachments/assets/91881b65-90e4-42e7-bf0b-78f2d894fd21)
![image](https://github.com/user-attachments/assets/71b13bb5-36b7-48cb-8bf5-8c0f2f1ca8d3)
![image](https://github.com/user-attachments/assets/6bc10e62-9896-4bb8-9381-f354441a8177)
![image](https://github.com/user-attachments/assets/3ff6b1ee-c073-4a17-8d8a-cff430ff3b70)

</details>
</br>

7. As a user, I want to know my score

|Feature|Action|Expected Result|Outcome|
|---|---|---|---|
|Scoreboard|Players are informed of their score at the end of the game|When the game ends the user is told their score and if it was over half the total achieveable score through 2 messages|Works as expected|
|Main Menu|Option 2 - Scoreboard|When the player, Selects the scoreboard option they can see a table of all of the players and their scores, Including their own score|Works as expected|
<details>
 <summary>Images</summary>

![image](https://github.com/user-attachments/assets/0f33507f-49ea-4a0f-88d0-01d7aec371aa)
![image](https://github.com/user-attachments/assets/645b5970-6cda-4a9e-be76-ae336f278ad3)

</details>
</br>

8. As a user, I want to be able to play multiple times after logging in

|Feature|Action|Expected Result|Outcome|
|---|---|---|---|
|Login|Login boolean is True when the player logs in|When the player logs in the login bool is turned to True, That way the player can play multiple times without having to login again|Works as expected|

<details>
 <summary>Images</summary>

![image](https://github.com/user-attachments/assets/e24f7633-27bb-4b5a-a79c-eafffa565f43)

</details>
</br>

9. As a user, I want to see a scoreboard of all the best players

|Feature|Action|Expected Result|Outcome|
|---|---|---|---|
|Main Menu|Option 2 - Scoreboard|When the player, Selects the scoreboard option they can see a table of all of the players and their scores|Works as expected|

<details>
 <summary>Images</summary>

![image](https://github.com/user-attachments/assets/0f33507f-49ea-4a0f-88d0-01d7aec371aa)

</details>
</br>

10. As a user, I want to be able to login if I return

|Feature|Action|Expected Result|Outcome|
|---|---|---|---|
|Login|Player details saved to the database|When the player registers their details are saved to the database allowing them to login with the same email if they wish. Then a welcome back message is displayed|Works as expected|

<details>
 <summary>Images</summary>

![image](https://github.com/user-attachments/assets/956479c2-782d-44a9-ba50-42553119f796)

</details>
</br>

11. As a site owner, I want user to have feedback from the game in real-time

|Feature|Action|Expected Result|Outcome|
|---|---|---|---|
|Main Game|Players are informed of incorrect answers|When the user gives and incorrect answer they are informed|Works as expected|
|Main Game|Players are informed of correct answers|When the user gives and correct answer they are informed|Works as expected|

<details>
 <summary>Images</summary>

![image](https://github.com/user-attachments/assets/edfeb4c1-9e21-41ae-a4f0-c755dfbeac70)

</details>
</br>

12. As a site owner, I want my UI to be obvious and easy to navigate for my users

|Feature|Action|Expected Result|Outcome|
|---|---|---|---|
|Main Menu|Option 1 - Play Game|Users are presented with a clear option to start the game|Works as expected|
|Main Menu|Option 2 - How to play|Users are presented with a clear option to see the game rules and how to play|Works as expected|
|Main Menu|Option 3 - Scoreboard|Users are presented with a clear option to see the scoreboard|Works as expected|
|Main Menu|Option 4 - Quit|Users are presented with a clear option to quit the game|Works as expected|
|Scoreboard|Press any key to quit|The user is able to press any key to return to the main menu|Works as expected|
|How to play|Press any key to quit|The user is able to press any key to return to the main menu|Works as expected|
|End Screen|Press any key to quit|The user is able to press any key to return to the main menu|Works as expected|


<details>
 <summary>Images</summary>

![image](https://github.com/user-attachments/assets/4d8748ae-1cb0-4d41-b450-eebff03972dd)
![image](https://github.com/user-attachments/assets/b413da7f-69f5-4391-a304-a4e330c3ca45)
![image](https://github.com/user-attachments/assets/71590224-f065-433c-861d-935d9029c5f0)
![image](https://github.com/user-attachments/assets/7c60c3a1-a145-4d24-ad0a-80f0099027ef)
![image](https://github.com/user-attachments/assets/2f4151f1-59c4-41ed-bbd6-8a93c023f6b6)
![image](https://github.com/user-attachments/assets/c89a3673-749e-4764-b630-abf42d8eaaa0)

</details>
</br>

13. As a site owner, I want the users names and emails to be saved in a google spreadsheet

|Feature|Action|Expected Result|Outcome|
|---|---|---|---|
|Register|Prompt the user for their details|When the user registers they are asked for their name and email. If the email already exists it will notify the player. If it does not the details will be added to the spreadsheet|Works as expected|

<details>
 <summary>Images</summary>

![image](https://github.com/user-attachments/assets/6c2eb791-343e-4ae5-895e-873f1040c7e4)
![image](https://github.com/user-attachments/assets/df3ccaf0-c903-42d3-bce1-d584363213c2)

</details>
</br>

14. As a site owner, I want the user to know if there was a wrong input

|Feature|Action|Expected Result|Outcome|
|---|---|---|---|
|Feedback throughout the game|Players are informed of incorrect inputs|When the user inputs and incorrect option they are informed until the input is valid|Works as expected|
|Feedback throughout the validation|Players are informed of incorrect inputs|When the user inputs incorrect information they are informed and validation will only continue when the input is correct|Works as expected|

<details>
 <summary>Images</summary>

![image](https://github.com/user-attachments/assets/7bcd358e-8eec-4c9d-b77c-8d08883ff3bd)
![image](https://github.com/user-attachments/assets/8909a981-ecd0-4ccb-85e2-a0e725d8ac6d)
![image](https://github.com/user-attachments/assets/0faf713e-2f53-40db-a9ed-785a89263399)
![image](https://github.com/user-attachments/assets/91881b65-90e4-42e7-bf0b-78f2d894fd21)
![image](https://github.com/user-attachments/assets/71b13bb5-36b7-48cb-8bf5-8c0f2f1ca8d3)
![image](https://github.com/user-attachments/assets/6bc10e62-9896-4bb8-9381-f354441a8177)
![image](https://github.com/user-attachments/assets/3ff6b1ee-c073-4a17-8d8a-cff430ff3b70)

</details>
</br>
 
15. As a site owner, I want the users data to be validated to check if its correct

|Feature|Action|Expected Result|Outcome|
|---|---|---|---|
|Email Validator|Emails are validated when the user inputs them|When the user inputs their email it is checked with an email validator to see if it is correct, if not an error will pop up|Works as expected|

<details>
 <summary>Images</summary>

![image](https://github.com/user-attachments/assets/8cd0f153-cba3-4839-9e78-364acef0cc3e)

</details>
</br>

16. As a site owner, I want the user to be able to choose if they want to upload their score

|Feature|Action|Expected Result|Outcome|
|---|---|---|---|
|Scoreboard/End Screen prompt|User is prompted if they want to upload their score|When the user has answered all questions they are prompted, with if they want to upload their score to the scoreboard|Works as expected|

<details>
 <summary>Images</summary>

![image](https://github.com/user-attachments/assets/62f82c00-5731-4d59-8463-722b6146fd73)

</details>
</br>

17. As a site owner, I want the user to be able to login after closing the game

|Feature|Action|Expected Result|Outcome|
|---|---|---|---|
|Login|Player details saved to the database|When the player registers their details are saved to the database allowing them to login with the same email if they wish. Then a welcome back message is displayed|Works as expected|

<details>
 <summary>Images</summary>

![image](https://github.com/user-attachments/assets/956479c2-782d-44a9-ba50-42553119f796)

</details>
</br>

## Bugs

|Bug|Fix|
|---|---|
|User could enter nothing for the question and it would move on|Made it so it re-asks the question by adding the input again|
|Infinite loop when entering nothing into the "Have you played before" Input|Made it so instead of continuing the while loop, It re-asks the input|
|Colors were not loading properly|Imported the file correctly|
|Bug where the users name would not load to the scoreboard|Corrected it so it passed the name as before it was not passing the name correctly|
|Players could register with an email more than once|Added a function which loops through all emails|
|Game would not load correctly due to an error with the questions|Made questions_answer into a class instead of a function which resolved the issue|
|Message for the player not having a good score would not appear|Adjusted the score for the player so it checks for the correct amount|

## Validation
The original tool recommended by Code Institute([PEP8 Validator](http://pep8online.com/) is down or has been taken off the internet, Therefore I used an online python code check called pythorium to check for any syntax errors and a library call pycodestyle to check for PEP8 validation:

<details>
 <summary>Run.py</summary>

![image](https://github.com/user-attachments/assets/3c0c637f-bed9-4023-9884-f5c55a138b41)
![image](https://github.com/user-attachments/assets/1068c564-7d13-44a7-8f37-da98f5675b64)

</details>

<details>
 <summary>validation.py</summary>

![image](https://github.com/user-attachments/assets/3bb77a82-f782-4ad8-bec4-9788515f8f14)
![image](https://github.com/user-attachments/assets/be76938d-f645-4fd9-bcbc-cd1262b4c8c4)

</details>

<details>
 <summary>test_validation.py</summary>

![image](https://github.com/user-attachments/assets/23e467ce-6652-4249-855d-f45cdf9abc27)
![image](https://github.com/user-attachments/assets/e981c4ff-c016-48c2-9fe8-e85e9b223b43)

</details>

## Deployment

### Heroku Deployment

Log in to your account at heroku.com.
Create a new app, add a unique app name and choose your region.
Click on create app.
Go to "Settings".
Under Config Vars store any sensitive data in .json file. Name 'Key' field, copy the .json file paste it to 'Value' field. Also add a key 'PORT' and value '8000'.
Add required buildpacks. For this project, I set up 'Python' and 'node.js' in that order.
Go to "Deploy" and select "GitHub" in "Deployment method"
To link up the Heroku app to our Github repository code enter your repository name, click 'Search' and then 'Connect' when it shows below.
Choose the branch you want to buid your app from.
Wait for the app to build. Once ready you will see the “App was successfully deployed” message and a 'View' button to take you to your deployed link.

### Forking the GitHub Repository
1. Go to the GitHub repository
2. Click on Fork button in top right corner
3. You will then have a copy of the repository in your own GitHub account.

Making a Local Clone
1. Go to the GitHub repository
2. Locate the Code button above the list of files and click it
3. Highlight the "HTTPS" button to clone with HTTPS and copy the link
4. Open Git Bash
5. Change the current working directory to the one where you want the cloned directory
6. Type git clone and paste the URL from the clipboard ($ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY)
7. Press Enter to create your local clone

## Credits

### Images
- Flaticon was used to finding an icon for my page
- Favicon was used to format the icon into something useable for my websit

### Code
- [ASCII Art Archive](https://www.asciiart.eu/image-to-ascii) For allowing me to change an image to ASCII art.
- Code Institute - for the Git template IDE and "Love Sandwiches" Project which helped with setting up the google sheet and google drive API.
- [gspread documentation](https://docs.gspread.org/en/latest/user-guide.html) explained to me how to get a certain cells values which was immensly helpful.
- [Stack Overflow](https://stackoverflow.com/questions) - Helped me with several errors and different fixes

## Acknowledgements

First and foremost, I would like to give a special thank you to my wonderful girlfriend Jasmine, whose support has made managing a full-time job, Open University, and Code Institute submissions possible.

Special thank you also to Mo Shami, My mentor, whose help and guidance has been truly invaluable to me.

The Live link to this repository can be found here - https://github.com/LewisBull2303/CL_P3_One_Piece_Quiz
