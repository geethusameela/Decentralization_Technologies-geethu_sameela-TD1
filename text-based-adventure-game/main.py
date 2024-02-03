# main.py
from .story.chapter1 import start_chapter_one
from choices.decision_tree import make_decision
from players import Player

def display_text(text):
    print(text)
def display_formatted_text(player_name, chapter_title):


def display_intro():
    print("Welcome to the Text-Based Adventure Game!")
    print("You find yourself in a mysterious world. Your decisions will shape your destiny.")

def get_player_name():
    return input("Enter your character's name: ")

def main():
    display_intro()

    # Create a player
    player_name = get_player_name()
    player = Player(player_name)

    # Start the first chapter
    start_chapter_one(player)

    # Game loop
    while True:
        # Display player's inventory
        player.display_inventory()

        # Get player's decision
        options = ['Continue the journey', 'Check inventory', 'Quit']
        player_choice = make_decision(options)

        # Process player's decision
        if player_choice == 'Continue the journey':
            # Add more story content based on the continued journey choice
            print("You venture deeper into the unknown.")
        elif player_choice == 'Check inventory':
            player.display_inventory()
        elif player_choice == 'Quit':
            print("Thanks for playing! See you next time.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
