import time

def print_pause(message, delay=2):
    print(message)
    time.sleep(delay)

def intro():
    print_pause("You find yourself in a dark, dense forest.")
    print_pause("The air is cool, and the sounds of night echo around you.")
    print_pause("Suddenly, you see two paths in front of you.")
    print_pause("One path leads to a distant light, and the other disappears into the darkness.")

def first_choice():
    print("Enter 1 to follow the path toward the light.")
    print("Enter 2 to take the dark path.")
    print("Enter 3 to stay where you are and make a camp.")
    choice = input("What would you like to do? (1, 2, or 3): ")
    if choice == '1':
        light_path()
    elif choice == '2':
        dark_path()
    elif choice == '3':
        make_camp()
    else:
        print("Please enter a valid option.")
        first_choice()

def light_path():
    print_pause("You walk towards the light and find a cozy cabin.")
    print_pause("An old woman opens the door and invites you in.")
    print_pause("She offers you a hot cup of tea, and you feel safe for the night.")
    print_pause("Suddenly, she asks you to help her with a task in the morning.")
    print("Enter 1 to agree to help her.")
    print("Enter 2 to politely decline and leave the cabin.")
    print("Enter 3 to explore the cabin on your own.")
    choice = input("What would you like to do? (1, 2, or 3): ")
    if choice == '1':
        help_old_woman()
    elif choice == '2':
        leave_cabin()
    elif choice == '3':
        explore_cabin()
    else:
        print("Please enter a valid option.")
        light_path()

def help_old_woman():
    print_pause("The old woman smiles and thanks you.")
    print_pause("She takes you to a hidden garden behind the cabin.")
    print_pause("You spend the day helping her tend to the plants, and she rewards you with a magical amulet.")
    print_pause("Congratulations! You have earned the amulet of protection and survived the forest.")
    print_pause("The old woman also tells you about a secret exit from the forest.")
    print_pause("With the amulet and her guidance, you safely find your way out.")
    print_pause("Congratulations! You have successfully escaped the forest.")

def leave_cabin():
    print_pause("You politely decline and decide to leave the cabin.")
    print_pause("As you walk away, you hear strange noises coming from the forest.")
    print_pause("Suddenly, you are surrounded by shadows, and you realize you are not alone.")
    print_pause("Game over. You did not survive the night.")

def explore_cabin():
    print_pause("You decide to explore the cabin on your own.")
    print_pause("You find a strange, locked chest in the corner of the room.")
    print("Enter 1 to try to open the chest.")
    print("Enter 2 to leave the chest alone.")
    choice = input("What would you like to do? (1 or 2): ")
    if choice == '1':
        open_chest()
    elif choice == '2':
        print_pause("You decide to leave the chest alone and go back to rest.")
        print_pause("The old woman thanks you for not meddling with her belongings, and you spend a peaceful night in the cabin.")
        print_pause("Congratulations! You have survived the night.")
    else:
        print("Please enter a valid option.")
        explore_cabin()

def open_chest():
    print_pause("You manage to open the chest, and inside you find a glowing crystal.")
    print_pause("The old woman catches you and becomes furious.")
    print_pause("She casts a spell, and you find yourself turned into a statue.")
    print_pause("Game over. You did not survive the night.")

def dark_path():
    print_pause("You walk down the dark path, stumbling over branches.")
    print_pause("Suddenly, you hear a growl behind you.")
    print_pause("A large wolf appears and blocks your path.")
    print_pause("Enter 1 to try to fight the wolf.")
    print_pause("Enter 2 to climb a nearby tree.")
    print_pause("Enter 3 to use a nearby cave for shelter.")
    choice = input("What would you like to do? (1, 2, or 3): ")
    if choice == '1':
        fight_wolf()
    elif choice == '2':
        climb_tree()
    elif choice == '3':
        hide_in_cave()
    else:
        print("Please enter a valid option.")
        dark_path()

def fight_wolf():
    print_pause("You decide to fight the wolf with all your strength.")
    print_pause("The wolf is strong, but you manage to grab a nearby branch and fend it off.")
    print_pause("You survive, but you are injured and must find help soon.")
    print_pause("Enter 1 to continue down the path in search of help.")
    print_pause("Enter 2 to rest and regain your strength.")
    choice = input("What would you like to do? (1 or 2): ")
    if choice == '1':
        continue_path()
    elif choice == '2':
        rest()
    else:
        print("Please enter a valid option.")
        fight_wolf()

def continue_path():
    print_pause("You continue down the path, limping slightly.")
    print_pause("Eventually, you come across a village where the villagers help you recover.")
    print_pause("Congratulations! You have survived and found safety in the village.")
    print_pause("The villagers tell you about an old, enchanted tree that can grant wishes.")
    print("Enter 1 to visit the enchanted tree.")
    print("Enter 2 to stay in the village and rest.")
    choice = input("What would you like to do? (1 or 2): ")
    if choice == '1':
        enchanted_tree()
    elif choice == '2':
        stay_in_village()
    else:
        print("Please enter a valid option.")
        continue_path()

def enchanted_tree():
    print_pause("You decide to visit the enchanted tree.")
    print_pause("The tree is massive, with branches that seem to touch the sky.")
    print_pause("You make a wish, and the tree grants you a safe passage out of the forest.")
    print_pause("Congratulations! You have survived and been granted a safe journey home.")

def stay_in_village():
    print_pause("You decide to stay in the village and rest.")
    print_pause("The villagers provide you with food and shelter.")
    print_pause("After a few days of rest, you feel strong enough to continue your journey.")
    print_pause("With their help, you safely make your way out of the forest.")
    print_pause("Congratulations! You have survived and escaped the forest.")

def rest():
    print_pause("You decide to rest, but the forest is dangerous.")
    print_pause("While resting, the wolf returns with its pack.")
    print_pause("Game over. You did not survive the night.")

def climb_tree():
    print_pause("You quickly climb up a nearby tree to escape the wolf.")
    print_pause("The wolf circles below for a while before eventually leaving.")
    print_pause("You spend the rest of the night in the tree, cold but safe.")
    print_pause("In the morning, you see a mysterious figure walking through the forest.")
    print("Enter 1 to call out to the figure.")
    print("Enter 2 to stay silent and observe.")
    choice = input("What would you like to do? (1 or 2): ")
    if choice == '1':
        call_out()
    elif choice == '2':
        stay_silent()
    else:
        print("Please enter a valid option.")
        climb_tree()

def call_out():
    print_pause("You call out to the figure, and they turn towards you.")
    print_pause("It turns out to be a forest ranger, and they help you find your way out of the forest.")
    print_pause("Congratulations! You have survived and been rescued.")

def stay_silent():
    print_pause("You decide to stay silent and observe.")
    print_pause("The figure passes by, and you remain in the tree until it's safe to come down.")
    print_pause("You manage to find your way out of the forest on your own.")
    print_pause("Congratulations! You have survived.")

def hide_in_cave():
    print_pause("You run towards a nearby cave and hide inside.")
    print_pause("The wolf sniffs around but eventually loses interest and leaves.")
    print_pause("Inside the cave, you discover a hidden passage leading deeper underground.")
    print("Enter 1 to explore the passage.")
    print("Enter 2 to stay near the entrance and wait for morning.")
    choice = input("What would you like to do? (1 or 2): ")
    if choice == '1':
        explore_passage()
    elif choice == '2':
        print_pause("You decide to stay near the entrance and wait for morning.")
        print_pause("You make it through the night safely, and as dawn breaks, you leave the cave.")
        print_pause("Congratulations! You have survived the night.")
    else:
        print("Please enter a valid option.")
        hide_in_cave()

def explore_passage():
    print_pause("You venture deeper into the cave, following the hidden passage.")
    print_pause("The passage leads to an underground chamber filled with ancient artifacts.")
    print_pause("Among the artifacts, you find a powerful sword, which you take with you.")
    print_pause("With the sword in hand, you feel more confident about facing the dangers of the forest.")
    print_pause("As you exit the cave, you encounter a mysterious creature guarding the exit.")
    print("Enter 1 to fight the creature with your new sword.")
    print("Enter 2 to try to negotiate with the creature.")
    choice = input("What would you like to do? (1 or 2): ")
    if choice == '1':
        fight_creature()
    elif choice == '2':
        negotiate_creature()
    else:
        print("Please enter a valid option.")
        explore_passage()

def fight_creature():
    print_pause("You decide to fight the creature with your new sword.")
    print_pause("The sword glows as you strike, and the creature is defeated.")
    print_pause("You successfully make it out of the cave and find your way out of the forest.")
    print_pause("Congratulations! You have survived and escaped the forest.")

def negotiate_creature():
    print_pause("You decide to try to negotiate with the creature.")
    print_pause("The creature listens and, seeing your bravery, allows you to pass.")
    print_pause("You make it out of the cave safely and continue your journey out of the forest.")
    print_pause("Congratulations! You have survived and escaped the forest.")

def make_camp():
    print_pause("You decide to stay where you are and make a camp.")
    print_pause("You gather some wood and build a small fire to keep warm.")
    print_pause("The fire keeps the wild animals away, and you manage to rest peacefully through the night.")
    print_pause("In the morning, you find a map someone left near your camp.")
    print("Enter 1 to follow the map.")
    print("Enter 2 to ignore the map and explore on your own.")
    choice = input("What would you like to do? (1 or 2): ")
    if choice == '1':
        follow_map()
    elif choice == '2':
        explore_on_own()
    else:
        print("Please enter a valid option.")
        make_camp()

def follow_map():
    print_pause("You decide to follow the map, which leads you to a hidden path out of the forest.")
    print_pause("Following the map, you safely make your way out and find a nearby village.")
    print_pause("Congratulations! You have survived and found safety.")

def explore_on_own():
    print_pause("You decide to explore the forest on your own without following the map.")
    print_pause("After hours of wandering, you come across a hidden waterfall with fresh water.")
    print_pause("You rest, drink some water, and eventually find your way out of the forest.")
    print_pause("Congratulations! You have survived the forest.")

def encounter_forest_spirit():
    print_pause("As you continue your journey, you encounter a forest spirit.")
    print_pause("The spirit offers you a deal: safe passage in exchange for a task.")
    print("Enter 1 to accept the spirit's deal.")
    print("Enter 2 to refuse and find your own way.")
    choice = input("What would you like to do? (1 or 2): ")
    if choice == '1':
        accept_spirit_deal()
    elif choice == '2':
        refuse_spirit_deal()
    else:
        print("Please enter a valid option.")
        encounter_forest_spirit()

def accept_spirit_deal():
    print_pause("You accept the spirit's deal and are given a magical lantern to guide you.")
    print_pause("The spirit leads you through the forest safely, and you make it out alive.")
    print_pause("Congratulations! You have survived and escaped the forest with the help of the spirit.")

def refuse_spirit_deal():
    print_pause("You refuse the spirit's deal, and the forest grows darker.")
    print_pause("You struggle to find your way, and the shadows seem to follow you.")
    print_pause("Game over. You did not survive the night.")

def play_game():
    intro()
    first_choice()

    while True:
        play_again = input("Would you like to play again? (yes or no): ")
        if play_again.lower() == 'yes':
            play_game()
        elif play_again.lower() == 'no':
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Please enter 'yes' or 'no'.")

play_game()
