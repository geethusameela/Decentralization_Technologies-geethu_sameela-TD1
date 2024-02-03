# story/chapter1.py

def start_chapter_one():
    print("You wake up in a mysterious forest. The air is thick with an otherworldly energy.")
    print("As you look around, you notice two paths ahead of you.")

    choice = input("Do you want to go left (L) or right (R)? ").lower()

    if choice == 'l':
        return go_left()
    elif choice == 'r':
        return go_right()
    else:
        return "Invalid choice. Try again."

def go_left():
    print("You chose the left path.")
    print("As you venture deeper, you encounter a mystical creature.")

    choice = input("Do you want to approach the creature (A) or try to sneak past it (S)? ").lower()

    if choice == 'a':
        return approach_creature()
    elif choice == 's':
        return sneak_past_creature()
    else:
        return "Invalid choice. Try again."

def go_right():
    print("You chose the right path.")
    print("You find a hidden passage leading to a magical realm.")

    choice = input("Do you want to explore the magical realm (E) or continue on the path (C)? ").lower()

    if choice == 'e':
        return explore_magical_realm()
    elif choice == 'c':
        return continue_on_path()
    else:
        return "Invalid choice. Try again."

def approach_creature():
    print("You cautiously approach the mystical creature.")
    print("It turns out to be a friendly forest guardian who guides you to a secret garden.")

    # Add more story content and choices based on the player's decision

def sneak_past_creature():
    print("You decide to silently sneak past the mystical creature.")
    print("You successfully avoid detection and find a hidden treasure chest.")

    # Add more story content and choices based on the player's decision

def explore_magical_realm():
    print("You enter the magical realm and discover a world filled with enchanting wonders.")
    print("As you explore, you encounter magical beings and learn about the realm's history.")

    # Add more story content and choices based on the player's decision

def continue_on_path():
    print("You choose to continue on the path through the magical realm.")
    print("The path leads you to a mystical portal that transports you to another dimension.")

    # Add more story content and choices based on the player's decision
