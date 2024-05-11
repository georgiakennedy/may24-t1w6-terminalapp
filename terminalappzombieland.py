from zombielandfunctions import pick_tools, fight_zombies1, fight_zombies2, fight_zombies3, reach_safety

import emoji
import csv
import os

from colored import Fore, Back, Style

titlecolour: str = f'{Style.BOLD}{Fore.RED}{Back.BLACK}'
narrativecolours: str = f'{Fore.RED}{Back.BLACK}'
textcolour: str = f'{Fore.WHITE}{Back.BLACK}'
errormessage: str = f'{Style.BOLD}{Fore.RED}{Back.BLACK}'
confirmingstyle: str = f'{Style.BOLD}{Fore.WHITE}{Back.BLACK}'
lifecount: str = f'{Style.BOLD}{Fore.RED}{Back.BLACK}'
gamecomplete: str = f'{Style.BOLD}{Fore.GREEN}{Back.BLACK}'

print(emoji.emojize(f"{titlecolour}Zombieland :zombie:{Style.reset}"))

user_name = input(f"Welcome to Zombieland! What is your name? ")

print(f"{narrativecolours}{user_name}... The Zombie Apocalypse has just begun. You're hiding in your house until you hear your front door crash in, and slow footsteps begin roaming around downstairs.\nThe zombies have broken in, and time is running out. Quickly, you need to gather essential items to survive. You search around your bedroom and find a small backpack that could fit up to 3 items in it. You don't have much time, so this will have to do.\nAfter a few minutes, you've found a few items you think could help you on your travels to safety, but you can only select 3.{Style.reset}")
      
print("What items are you taking? Choose wisely, for your survival depends on it.")

def main():
    player_lives = 2
    pick_tools(player_lives)

    fight_zombies1(player_lives)
    fight_zombies2(player_lives)
    fight_zombies3(player_lives)


main()