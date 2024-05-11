# Georgia Kennedy T1A3 Zombieland Python Application

## Links

Source Repository Link:

Project Management Link: https://trello.com/invite/b/1MECdoKe/ATTI7d48bdc8eef9c415bf4f6e684f45392fADEAA72F/t1a3-survival-game

## About the App

Zombieland is a mini survival game set in a post-apocalyptic world. The goal for the user is to navigate their way to safety. The user will have a backpack with limited space where they can store a few items to help them along the way. They’ll be faced with a few different situations where they have to choose an object from their backpack to help them get out of the situation in one piece. If they fail the challenge, they’ll lose a “life”. The users will start with 2 lives, and if they lose both of them before they reach the end of the game, they lose. 

## Help Documentation
Insert Here

### Dependencies
Note: This app requires Python 3 to be installed on your machine. To check if Python3 is installed on your machine, type the following into your terminal:
Python3 --version
If your machine has Python installed, it’ll return something along the lines of Python 3.8.1 or whatever version your machine has. 

If your machine does not have Python3 downloaded, you can go to the official Python website and follow the steps at https://www.python.org/downloads/ . 

This app uses the following python packages which will install automatically:
-	Colored – Ensure you have no colour theme on your VS Code for the colours to work correctly.
-	Csv
-	Os
-	Emoji


## Game Instructions
The user will need to follow along with the story, choose items to fill their backpack, choose what items to enter a mini game with.
When you enter the app, you'll be prompted to enter your name.

Once this information has been entered, you'll receive the first section of narration. Narration throughout the app is written in red. Read through the introduction carefully. to get an idea on the backstory of the game.
After you've read the introduction, you'll be prompted to select your items.
Enter 1 to select the First Aid Kit.
Enter 2 to select the Water Purification Tablets.
Enter 3 to select the Crowbar.
Enter 4 to select the Energy Bars.
Enter 5 to select the Flashlight.

<img width="533" alt="image" src="https://github.com/georgiakennedy/may24-t1w6-terminalapp/assets/158373465/458d2bac-9e7f-4128-9d4a-c68aca47fb59">

Once you have selected your items, confirm your selection by typing "yes' or "no”. Yes will continue the storyline, no will make you reselect your items.

Once you have selected your items, you'll follow on with the storyline. Read the given scenario, then you'll be prompted to select a tool from your backpack that you think will get you out of the challenge safely. The app will ask you for your input, you'll need to enter the number corresponding to the item you'd like to use. For example:
1.	Flashlight
2.	Medical Kit
3.	Crowbar
<img width="555" alt="image" src="https://github.com/georgiakennedy/may24-t1w6-terminalapp/assets/158373465/518f5f5c-56e1-4041-ab07-80ed4a3bb301">

By selecting, "2". you will be using the Medical Kit to help you in the situation

This will repeat 2 more times and you'll need to repeat these steps for the next 2 scenarios.
Each player gets 2 lives. If you lose all your lives, you'll be presented with a "Game Over" message. followed by exiting the program.


## Program Features
### Feature 1: Backpack Storing
The backpack storing feature in my application allows the user to select and store their chosen tools in a backpack. The selected tools are stored in a CSV file (backpackitems.csv) so that they can be retrieved later. 

How the feature works:

When the pick_tools() function is called, a list called backpack_items is created to store the selected tools. The function then displays a list of tools that the user can choose from, numbered 1 to 5. These include, a medical kit, water purification tablets, crowbar, energy bars and a flashlight. The user is then prompted to enter the number corresponding to the tool they want to select. They can choose up to 3 tools. The users choice is then processed and the selected tool is added to the backpack_items list if it’s not already in there. After the user has selected three tools or reached the maximum limit, the function writes the selected tools in the CSV file and will display the selected tools to the user. The user can then confirm if they have selected the correct tools by typing “yes” or “no”. Once the user is happy with their choices, the function proceeds to the fight_zombies1 function. When the user selects tools to use in scenarios, the list is updated and the new selection is written back to the CSV file. 

<img width="550" alt="image" src="https://github.com/georgiakennedy/may24-t1w6-terminalapp/assets/158373465/f696f297-2b92-4c63-903f-5541c37960e4">

<img width="214" alt="image" src="https://github.com/georgiakennedy/may24-t1w6-terminalapp/assets/158373465/db7023d8-bcac-428d-adf2-edfb5f5f945e">



