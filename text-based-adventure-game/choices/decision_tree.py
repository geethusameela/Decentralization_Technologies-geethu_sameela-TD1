# choices/decision_tree.py

def make_decision(player_choice):
    if player_choice == 'a':
        return decision_a()
    elif player_choice == 'b':
        return decision_b()
    else:
        return "Invalid choice. Try again."

def decision_a():
    print("You chose option A.")
    # Add more story content and choices based on the player's decision

def decision_b():
    print("You chose option B.")
    # Add more story content and choices based on the player's decision
