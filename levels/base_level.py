# levels/base_level.py

class Room:
    def __init__(self, name, description, items, clues, note_texts):
        self.name = name
        self.description = description
        self.items = items
        self.clues = clues
        self.note_texts = note_texts

        self.found_clues = {}  # item name -> bool
        self.clues_found_count = 0

        # Each Room subclass will define its own special reward item
        self.room_item = "None"

    def play(self):
        print(f"\nYou enter the {self.name}.")
        print(self.description)

        while self.clues_found_count < len(self.clues):
            print(f"\nWhat do you want to search? (Options: {', '.join(self.items)})")
            choice = input("> ").lower().strip()

            if choice in self.items:
                if choice in self.clues and not self.found_clues.get(choice, False):
                    print(f"\nYou found a clue! Here's what the note says:\n{self.note_texts[choice]}")
                    self.found_clues[choice] = True
                    self.clues_found_count += 1
                elif choice in self.clues and self.found_clues.get(choice, False):
                    print("You already found this clue.")
                else:
                    print("You search around but find nothing unusual.")
            else:
                print("Invalid choice, please try again.")

        print(f"\nYou have found all clues in the {self.name}!")
        print(f"You discover a special item: {self.room_item}")

        # Return the special room item as reward
        return self.room_item


class BaseLevel:
    def __init__(self, name, intro_paragraph, rooms):
        self.name = name
        self.intro_paragraph = intro_paragraph
        self.rooms = rooms
        self.collected_items = []

    def play(self):
        print(f"\n{self.name}\n")
        print(f"Welcome to {self.name}")
        print(f"{self.intro_paragraph}\n")

        for room in self.rooms:
            item = room.play()
            self.collected_items.append(item)

        print("\nYou have collected all special items from the rooms:")
        for itm in self.collected_items:
            print(f"- {itm}")

        # Here you can add logic to check if these items unlock the exit or next clue
        if self.can_exit():
            print("\nCongratulations! You have gathered all necessary items and solved the Villa mystery!")
            print("You can now proceed to the next level.")
        else:
            print("\nYou are missing some crucial items. Keep searching!")

    def can_exit(self):
        # Check if all required special items are collected (3 for Villa)
        required_items = {"Ancient Key Fragment", "Silver Compass Piece", "Golden Locket"}
        return required_items.issubset(set(self.collected_items))
