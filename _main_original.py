import random

def intro():
    print("Escape the Mystery Dungeon!")
    print("\nInstructions:")
    print("You will find clues in each room that will lead you to the exit of the level.")
    print("That will allow you to solve the mystery of that level and move onto the next one.")
    print("You can type the name of an object you see in the room to search that object for a clue.")
    print("Once you found all the clues, you will be prompted to choose the next room you want to go into to search.")
    print("Once you find all the clues, you can leave the level! Have fun!")
    input("\nHit enter to start.\n")  # Wait for user to press Enter to start

def room_1():
    print("\nLevel 1: The Villa")
    print(" ")
    print("Room 1: The Study")
    print(" ")
    print("The Study is a cozy, dimly lit room filled with old bookshelves lined with dusty books.")
    print("A wooden desk sits in the center with papers scattered across it.")
    print("A fireplace crackles in the corner, its mantel adorned with trinkets and a clock ticking away.")
    print("There’s a large painting on the wall, and a comfy armchair near the window.")
    # in the final version of the game the options will be hidden after the description
    print("\nWhat do you want to search? (Options: books, desk, fireplace, clock, painting, armchair)")

    items = ['books', 'desk', 'fireplace', 'clock', 'painting', 'armchair']
    clues = ['puzzle piece', 'key', 'note']

    note_text = {
        'desk': "The note reads: 'The key you seek is hidden behind the painting.'",
        'books': "The note reads: 'Beware of the cracks in the floor, they may lead to something unknown.'",
        'fireplace': "The note reads: 'A hidden drawer lies beneath the desk, but only the clever will find it.'",
    }

    # Randomly shuffle both clues and items to assign clues to random items
    random.shuffle(items)
    random.shuffle(clues)

    # Dictionary to track which clues are assigned to which items
    clue_assignment = {items[i]: clues[i] for i in range(len(clues))}

    found_clues = {'puzzle piece': False, 'key': False, 'note': False}
    clues_found = 0

    while clues_found < 3:
        choice = input("> ").lower()

        if choice in clue_assignment:  # If the item is a valid option
            clue = clue_assignment[choice]
            if not found_clues[clue]:
                if clue == 'note':
                    print(f"You found a clue! You found a note.")
                    print(note_text.get(choice, "This note is blank."))
                else:
                    print(f"You found a clue! You found a {clue}.")
                found_clues[clue] = True
                clues_found += 1
            else:
                print("Sorry, no clue here.")
        elif choice in items:
            print("Sorry, no clue here.")
        else:  # Invalid choice
            print("Invalid choice. Please try again.")

    print("Let's go to the next room!")

def room_2():
    print("\nRoom 2: The Kitchen")
    print(" ")
    print("The kitchen smells of spices and fresh bread. A large stove sits in the corner with a pot boiling away.")
    print("The counters are cluttered with ingredients for baking, and a cabinet full of old cookware is to the side.")
    print("A small table is in the center with a fruit bowl, and there’s a pantry door on the far side of the room.")
    print("\nWhat do you want to search? (Options: stove, counters, cabinet, table, pantry)")

    items = ['stove', 'counters', 'cabinet', 'table', 'pantry']
    clues = ['puzzle piece', 'key', 'note']

    note_text = {
        'stove': "The note reads: 'If you find the right temperature, the secret will be revealed.'",
        'table': "The note reads: 'The key to the next room is hidden behind the pantry door.'",
        'pantry': "The note reads: 'Sometimes the ingredients to a puzzle are right in front of you.'",
    }

    random.shuffle(items)
    random.shuffle(clues)

    clue_assignment = {items[i]: clues[i] for i in range(len(clues))}

    found_clues = {'puzzle piece': False, 'key': False, 'note': False}
    clues_found = 0

    while clues_found < 3:
        choice = input("> ").lower()

        if choice in clue_assignment:
            clue = clue_assignment[choice]
            if not found_clues[clue]:
                if clue == 'note':
                    print(f"You found a clue! You found a note.")
                    print(note_text.get(choice, "This note is blank."))
                else:
                    print(f"You found a clue! You found a {clue}.")
                found_clues[clue] = True
                clues_found += 1
            else:
                print("Sorry, no clue here.")
        elif choice in items:
            print("Sorry, no clue here.")
        else:
            print("Invalid choice. Please try again.")

    print("Let's go to the next room!")

def room_3():
    print("\nRoom 3: The Basement")
    print(" ")
    print("The basement is dark and damp, with cobwebs hanging from the rafters. A workbench is set up in one corner,")
    print("cluttered with tools and half-finished projects. The floor is cold, and a large wooden crate sits against one wall.")
    print("A narrow staircase leads up to the kitchen, and a small window near the ceiling lets in faint light.")
    print("\nWhat do you want to search? (Options: workbench, crate, staircase, window)")

    items = ['workbench', 'crate', 'staircase', 'window']
    clues = ['puzzle piece', 'key', 'note']

    note_text = {
        'workbench': "The note reads: 'The puzzle pieces are scattered in the rooms. Find them all to unlock the door.'",
        'crate': "The note reads: 'Under the stairs, secrets wait for those who are brave enough to search.'",
        'staircase': "The note reads: 'The way out is closer than you think. Follow the clues carefully.'",
    }

    random.shuffle(items)
    random.shuffle(clues)

    clue_assignment = {items[i]: clues[i] for i in range(len(clues))}

    found_clues = {'puzzle piece': False, 'key': False, 'note': False}
    clues_found = 0

    while clues_found < 3:
        choice = input("> ").lower()

        if choice in clue_assignment:
            clue = clue_assignment[choice]
            if not found_clues[clue]:
                if clue == 'note':
                    print(f"You found a clue! You found a note.")
                    print(note_text.get(choice, "This note is blank."))
                else:
                    print(f"You found a clue! You found a {clue}.")
                found_clues[clue] = True
                clues_found += 1
            else:
                print("Sorry, no clue here.")
        elif choice in items:
            print("Sorry, no clue here.")
        else:
            print("Invalid choice. Please try again.")

    print("You found the last clue. The puzzle pieces show you the way out. You have the key to the exit! Let's go!")

def outro():
    print("\nYou solved the mystery of the Villa! Thank you for playing. Keep your eyes out for updates!")
    print("\nCredits:")
    print("Game created by: Jeff Tufts with help from LCC 161P and the Internet.")

def main():
    intro()
    room_1()
    room_2()
    room_3()
    outro()
    replay = input("\nWould you like to play again? (y/n): ").lower()
    if replay == 'y':
        main()
    else:
        print("Goodbye!")

if __name__ == "__main__":
    main()
