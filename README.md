# Georgia Kennedy T1A3 Zombieland Python Application

## Links

Source Repository Link: https://github.com/georgiakennedy/may24-t1w6-terminalapp

Project Management Link: https://trello.com/invite/b/1MECdoKe/ATTI7d48bdc8eef9c415bf4f6e684f45392fADEAA72F/t1a3-survival-game

## About the App

Zombieland is a mini survival game set in a post-apocalyptic world. The goal for the user is to navigate their way to safety. The user will have a backpack with limited space where they can store a few items to help them along the way. They’ll be faced with a few different situations where they have to choose an object from their backpack to help them get out of the situation in one piece. If they fail the challenge, they’ll lose a “life”. The users will start with 2 lives, and if they lose both of them before they reach the end of the game, they lose. 

## Help Documentation
You will need to install the following python packages:

Colored:

pip3 install colored

Emoji:

pip3 install emoji

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

### Feature 2: Life Count
The life count feature of my application keeps track of the players remaining lives as they progress through the game. The player starts with 2 lives and each time they fail a scenario, they lose a life. Once the player’s life count reaches 0, the game will end and display a game over message.

How the feature works: At the beginning of the game, the players life count will automatically set at 2 using the player_lives variable. As the player progresses through the game, they will encounter scenarios that could result in them losing a life depending on the tool they use. For example, if the player selects water purification tablets in the first scenario, they’ll lose a life as the required items are the crow bar or the energy bars. The command player_lives -= 1 is used to reduce the players life count by 1. The game will check the players life count at various points to determine the outcome. For example, if the players life count reaches 0, the game will end and exit the game. The life count is displayed to the user at the end of every outcome when they select an item to use.
<img width="736" alt="image" src="https://github.com/georgiakennedy/may24-t1w6-terminalapp/assets/158373465/e9f5d62a-61b5-49a6-940a-f51155ef2702">
<img width="513" alt="image" src="https://github.com/georgiakennedy/may24-t1w6-terminalapp/assets/158373465/202cab63-c4d5-4112-9e89-02044601ae7d">

### Feature 3: User Choice Impacts Program
This interactive feature allows users to input their own choices and select tools to overcome the challenges in the game.

How the feature works: Players are presented with a piece of narration that outlines the challenge and lists the available tools that they can choose from. The players are then prompted to input their tool selection. Once the player makes their selection, the game will determine the outcome based on their choice. This involves checking if the selected tool is the correct tool needed for the challenge and determines if the players choice will lead to a pass or a fail. The game will then provide feedback to the player, informing them of their outcome then will continue the game and present the user with a new challenge. 


## Application Error Testing & Handling
I decided to manually test my application to ensure each feature was working correctly. I started by checking that the application runs without any errors. I would interact with the application as if the user would. This included providing input, selecting options and navigating through the program. To test error handling, I would enter invalid items to ensure the application correctly responds to these and brings the user back to the correct path. I made sure to try all the tools in each scenario to ensure the user would receive the correct messages in response. I tested each specific feature to ensure it was all working. When testing the backpack storing feature, I made sure that the tools were stored correctly and retrieved accurately by opening the CSV file when I made my tool selection. I would also purposely lose lives to see if the game would end and exit when the player lost all the lives. 

### Testing the Backpack Feature:
When ensuring that the backpack feature was in working order, I made sure to select each tool that I wanted, then checked the CSV file to see if the items I chose were in there. I would then select “no” to repeat this process and choose my items again. When selecting “no”, the app would delete the CSV file and provide the user with a fresh one when choosing their items again. I also made sure to put in invalid items to ensure that the application would respond appropriately and prompt the user to re-input their tool selection. Another feature I tested was making sure that the application would respond appropriately when an item that had already been selected was chosen again. The app was able to inform the user that their tool was already selected, and prompted them to reselect an item.

### Testing the Life Count Feature:
In order to test if the life count feature was working correctly, I made sure to select incorrect choices on challenges. I would either select all incorrect choices, to which the game would respond by exiting the player early. I also would select incorrect choices on one challenge, which resulted in the player completing the game as they still had one life remaining.  

### Testing Scenarios:
User selects 1, 3 and 5:

User decides to use tool 3 in the first scenario, tool 1 in the second scenario and tool 5 in the final scenario. 
The program was able to respond appropriately to all these requests and the user was able to complete the game with no lives lost. 

User selects 1, 2 and 3:

User decides to use tool 3 in the first scenario, tool 1 in the second scenario and tool 2 in the final scenario.
The program was able to respond appropriately to all these requests. The user lost one life in the final scenario as this was the incorrect tool needed for this challenge.

User selects 2, 4 and 3:

User decides to use tool 2 in the first scenario, tool 4 in the second scenario and tool 3 in the final scenario.
The program was able to respond appropriately to all these requests. The user lost all lives as each of these tools weren’t the correct ones needed for the challenge. The players game ended before the last scenario as they lost 2 lives in the first two challenges. 


## Code Style 
For this project, I decided to use PEP 8 Code Styling Guide. More about this style guide can be found here: https://peps.python.org/pep-0008/

## Project Management 
To assist with project management, I created a Trello board which can be found here: https://trello.com/invite/b/1MECdoKe/ATTI7d48bdc8eef9c415bf4f6e684f45392fADEAA72F/t1a3-survival-game

I created 3 different lists (to do, doing and done) to help manage the workload, and keep track of what I was currently working on, what I needed to do, and what was already completed. I added little comments to each card I made so I could go back and read what I had done/what I needed to do in that particular card. 
