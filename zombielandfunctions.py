import csv
import os
import emoji

from colored import Fore, Back, Style

titlecolour: str = f'{Style.BOLD}{Fore.RED}{Back.BLACK}'
narrativecolours: str = f'{Fore.RED}{Back.BLACK}'
textcolour: str = f'{Fore.WHITE}{Back.BLACK}'
errormessage: str = f'{Style.BOLD}{Fore.RED}{Back.BLACK}'
confirmingstyle: str = f'{Style.BOLD}{Fore.WHITE}{Back.BLACK}'
lifecount: str = f'{Style.BOLD}{Fore.RED}{Back.BLACK}'
gamecomplete: str = f'{Style.BOLD}{Fore.GREEN}{Back.BLACK}'


def pick_tools(player_lives):
    global backpack_items

    print(emoji.emojize("1. First Aid Kit. :pill:"))
    print(emoji.emojize("2. Water Purification Tablets. :droplet:"))
    print(emoji.emojize("3. Crowbar. :pick:"))
    print(emoji.emojize("4. Energy Bar. :chocolate_bar:"))
    print(emoji.emojize("5. Flashlight. :flashlight:"))

    backpack_items = []

    file_name = "backpackitems.csv"

    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                backpack_items.extend(row)

    i = 0
    while i < 3:
        choice = input(f"Enter the number corresponding to tool {i + 1}: ")

        if choice == "1":
            tool = "First Aid Kit"
        elif choice == "2":
            tool = "Water Tablets"
        elif choice == "3":
            tool = "Crowbar"
        elif choice == "4":
            tool = "Energy Bars"
        elif choice == "5":
            tool = "Flashlight"
        else:
            print(f"{errormessage}Invalid choice. Please try again.{Style.reset}")
            continue

        if tool in backpack_items:
            print(f"{errormessage}{tool} is already in your backpack. Please choose another tool.{Style.reset}")
            continue

        backpack_items.append(tool)
        i += 1

    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        for tool in backpack_items:
            writer.writerow([tool])

    print("You have chosen the following tools:")
    for tool in backpack_items:
        print(tool)

    confirm = input(f"{confirmingstyle}Are you sure about your tool selection? (yes/no): {Style.reset}")
    if confirm.lower() == "no":
        backpack_items.clear()
        print("Your tool selection has been cleared. Please choose again.")

        if os.path.exists(file_name):
            os.remove(file_name)

        pick_tools(player_lives)
    elif confirm.lower() == "yes":
        fight_zombies1(player_lives)
    else:
        print(f"{errormessage}Invalid choice. Please try again.{Style.reset}")
        if os.path.exists(file_name):
            os.remove(file_name)
        pick_tools(player_lives)


def fight_zombies1(player_lives):
    global backpack_items
    player_lives = 2
    print(f"{narrativecolours}You cautiously make your way downstairs, gripping onto your backpack filled with your survival items. You reach the bottom of the stairs and see a group of zombies lurking in the living room. What item from your backpack are you using to safetly get out of this situation?{Style.reset}")
    for index, tool in enumerate(backpack_items):
        print(f"{index + 1}. {tool}")

    choice = input("Select a tool from your backpack to fight the zombies: ")

    if choice.isdigit() and int(choice) in range(1, len(backpack_items) + 1):
        chosen_tool = backpack_items[int(choice) - 1]

        if chosen_tool == "Energy Bars":
            print(emoji.emojize(f"{narrativecolours}:chocolate_bar: You hastily grab the energy bars, knowing that you'll need sustenance during your escape. As you head downstairs, you come face to face with a group of zombies. You quickly toss the energy bars behind them, distracting them momentarily. Taking advantage of the distraction, you slip past them and make a daring escape through the back door.{Style.reset}"))
            print(f"{lifecount}Lives left = {player_lives}{Style.reset}")
        elif chosen_tool == "Crowbar":
            print(emoji.emojize(f"{narrativecolours}:pick: Gripping the crowbar tightly, you make your way downstairs, ready to face the undead. With each step, your heart pounds in your chest. As you reach the ground floor, you come face to face with a group of zombies. You swing the crowbar with all your might, striking down the closest one. The others lunge at you, but you manage to fight them off, using your strength and the crowbar's leverage. You escape the house, battered but alive.{Style.reset}"))
            print(f"{lifecount}Lives left = {player_lives}{Style.reset}")
        elif chosen_tool == "First Aid Kit":
            print(emoji.emojize(f"{narrativecolours}:pill: Uh oh, without a weapon or means to defend yourself, you made yourself vulnerable.{Style.reset}"))
            player_lives -= 1
            print(f"{lifecount}Lives left = {player_lives}{Style.reset}")
        elif chosen_tool == "Water Tablets":
            print(emoji.emojize(f"{narrativecolours}:droplet: Uh oh, without a weapon or means to defend yourself, you made yourself vulnerable.{Style.reset}"))
            player_lives -= 1
            print(f"{lifecount}Lives left = {player_lives}{Style.reset}")
        elif chosen_tool == "Flashlight":
            print(emoji.emojize(f"{narrativecolours}:flashlight: Uh oh, without a weapon or means to defend yourself, you made yourself vulnerable.{Style.reset}"))
            player_lives -= 1
            print(f"{lifecount}Lives left = {player_lives}{Style.reset}")

        backpack_items.remove(chosen_tool)
    else:
        print(f"{errormessage}Invalid choice. Please try again.{Style.reset}")
        fight_zombies1(player_lives)

    file_name = "backpackitems.csv"

    if player_lives == 0:
        print(emoji.emojize(f"{errormessage}:zombie: Game Over. You have lost too many lives in the Zombie Apocalypse. Despite your efforts, the challenges proved too much, and your journey has come to an end.\nThe undead prevailed, and the world falls into darkness as you meet your fate.\nThank you for playing. Better luck next time.{Style.reset}"))
        if os.path.exists(file_name):
            os.remove(file_name)
        exit(1)
    
    fight_zombies2(player_lives)


def fight_zombies2(player_lives):
    global backpack_items

    print(f"{narrativecolours}You survived the first encounter with the zombies. However, the danger is far from over. You now find yourself in the chaotic streets, filled with the undead. You must navigate through the city to find safety.\nAs you make your way through the city streets, you encounter a group of zombies. Despite your best efforts to evade them, one manages to grab hold of you, causing a deep gash on your arm. Blood flows from the wound, and you feel a wave of dizziness wash over you.{Style.reset}")

    for index, tool in enumerate(backpack_items):
        print(f"{index + 1}. {tool}")

    choice = input("Select a tool from your backpack to help heal your wounds: ")

    if choice.isdigit() and int(choice) in range(1, len(backpack_items) + 1):
        chosen_tool = backpack_items[int(choice) - 1]

        if chosen_tool == "Energy Bars":
            print(emoji.emojize(f"{narrativecolours}:chocolate_bar: Uh oh, you were unable to heal your wound with energy bars and made yourself an easy target for the zombies to attack.{Style.reset}"))
            player_lives -= 1
            print(f"{lifecount}{lifecount}Lives left = {player_lives}{Style.reset}")
        elif chosen_tool == "Crowbar":
            print(emoji.emojize(f"{narrativecolours}:pick: Uh oh, you were unable to heal your wound with a crow bar and made yourself an easy target for the zombies to attack.{Style.reset}"))
            player_lives -= 1
            print(f"{lifecount}Lives left = {player_lives}{Style.reset}")
        elif chosen_tool == "First Aid Kit":
            print(emoji.emojize(f"{narrativecolours}:pill: You swiftly reach into your backpack and retrieve the first aid kit. With trembling hands, you rummage through the supplies to find the necessary items to clean and dress your wound. Despite the pain, you manage to patch yourself up, providing temporary relief and preventing further infection.{Style.reset}"))
            print(f"{lifecount}Lives left = {player_lives}{Style.reset}")
        elif chosen_tool == "Water Tablets":
            print(emoji.emojize(f"{narrativecolours}:droplet: Uh oh, you were unable to heal your wound with water purification tablets and made yourself an easy target for the zombies to attack.{Style.reset}"))
            player_lives -= 1
            print(f"{lifecount}Lives left = {player_lives}{Style.reset}")
        elif chosen_tool == "Flashlight":
            print(emoji.emojize(f"{narrativecolours}:flashlight: Uh oh, you were unable to heal your wound with a flashlight and made yourself an easy target for the zombies to attack.{Style.reset}"))
            player_lives -= 1
            print(f"{lifecount}Lives left = {player_lives}{Style.reset}")

        backpack_items.remove(chosen_tool)
    else:
        print(f"{errormessage}Invalid choice. Please try again.{Style.reset}")
        fight_zombies2(player_lives)

    file_name = "backpackitems.csv"

    if player_lives == 0:
        print(emoji.emojize(f"{errormessage}:zombie: Game Over. You have lost too many lives in the Zombie Apocalypse. Despite your efforts, the challenges proved too much, and your journey has come to an end.\nThe undead prevailed, and the world falls into darkness as you meet your fate.\nThank you for playing. Better luck next time.{Style.reset}"))
        if os.path.exists(file_name):
            os.remove(file_name)
        exit(1)

    fight_zombies3(player_lives)

def fight_zombies3(player_lives):
    global backpack_items
    print(f"{narrativecolours}Whew that was close! But you’re almost at the shelter! As you make your way through the dimly lit streets, the sun begins to set, casting shadows and making it difficult to see. The eerie darkness is a constant reminder of the lurking dangers that surround you.\nLet’s open your backpack and see if there’s anything in there that will help you see in the dark.{Style.reset}")

    for index, tool in enumerate(backpack_items):
        print(f"{index + 1}. {tool}")

    choice = input("Select a tool from your backpack to see in the dark: ")

    if choice.isdigit() and int(choice) in range(1, len(backpack_items) + 1):
        chosen_tool = backpack_items[int(choice) - 1]

        if chosen_tool == "Energy Bars":
            print(emoji.emojize(f"{narrativecolours}:chocolate_bar: Energy bars won’t help you see in the dark… You lost all visibility and came across a group of zombies. You try to defend yourself but it’s impossible to see where they’re all coming from. Your journey ends in tragedy.{Style.reset}"))
            player_lives -= 1
            print(f"Lives left = {player_lives}{Style.reset}")
        elif chosen_tool == "Crowbar":
            print(emoji.emojize(f"{narrativecolours}:pick: A crowbar won’t help you see in the dark… You lost all visibility and came across a group of zombies. You try to defend yourself with the crow bar but it’s impossible to see where they’re all coming from. Your journey ends in tragedy.{Style.reset}"))
            player_lives -= 1
            print(f"Lives left = {player_lives}{Style.reset}")
        elif chosen_tool == "First Aid Kit":
            print(emoji.emojize(f"{narrativecolours}:pill: A medical kit won’t help you see in the dark… You lost all visibility and came across a group of zombies. You try to defend yourself but it’s impossible to see where they’re all coming from. Your journey ends in tragedy.{Style.reset}"))
            player_lives -= 1
            print(f"Lives left = {player_lives}{Style.reset}")
        elif chosen_tool == "Water Tablets":
            print(emoji.emojize(f"{narrativecolours}:droplet: Water Purification Tablets won’t help you see in the dark… You lost all visibility and came across a group of zombies. You try to defend yourself but it’s impossible to see where they’re all coming from. Your journey ends in tragedy.{Style.reset}"))
            player_lives -= 1
            print(f"Lives left = {player_lives}{Style.reset}")
        elif chosen_tool == "Flashlight":
            print(emoji.emojize(f"{narrativecolours}:flashlight: You swiftly retrieve the flashlight from your backpack and switch it on, illuminating the path ahead. The beam of light cuts through the darkness, revealing hidden obstacles and potential threats. You’re able to navigate your way through the city without running into problems.{Style.reset}"))
            print(f"Lives left = {player_lives}{Style.reset}")

        backpack_items.remove(chosen_tool)
    else:
        print(f"{errormessage}Invalid choice. Please try again.{Style.reset}")
        fight_zombies3(player_lives)

    file_name = "backpackitems.csv"

    if player_lives == 0:
        print(emoji.emojize(f"{errormessage}:zombie: Game Over. You have lost too many lives in the Zombie Apocalypse. Despite your efforts, the challenges proved too much, and your journey has come to an end.\nThe undead prevailed, and the world falls into darkness as you meet your fate.\nThank you for playing. Better luck next time.{Style.reset}"))
        if os.path.exists(file_name):
            os.remove(file_name)
        exit(1)
    
    reach_safety(player_lives)

def reach_safety(player_lives):
    file_name = "backpackitems.csv"
    print(f"{gamecomplete}Congratulations! You've made it to the shelter, joining a group of survivors ready to face the challenges of the Zombie Apocalypse. Your choices and resourcefulness have paid off, and you can now rebuild and prepare for the battles ahead. Thank you for playing Apocalypse Rising.{Style.reset}")
    if os.path.exists(file_name):
            os.remove(file_name)
    exit(1)



