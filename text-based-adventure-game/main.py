 

# main.py
from .story.chapter1 import start_chapter_one
from .choices.decision_tree import make_decision

def get_player_choice():
    return input("Enter your choice: ")

def display_text(text):
    print(text)

def main():
    print("Welcome to the Text-based Adventure Game!")

    player_name = input("Enter your character's name: ")
    display_text(f"Hello, {player_name}! Your adventure begins.")

    start_chapter_one()

    while True:
        display_text("1. Enter the dark cave")
        display_text("2. Follow the riverbank")

        player_choice = get_player_choice()
        result = make_decision(player_choice)

        display_text(result)

if __name__ == "__main__":
    main()
