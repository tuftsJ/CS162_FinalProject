# main.py

from clue import Clue

def main():
    # Create clue objects
    key = Clue("Old Rusty Key")
    puzzle_piece = Clue("Corner Puzzle Piece")
    note = Clue("Crumbled Note")

    # Display initial clue names
    print("Initial clues:")
    print(key)
    print(puzzle_piece)
    print(note)

    # Update clue names using the property setter
    key.name = "Shiny Golden Key"
    puzzle_piece.name = "Middle Puzzle Piece"
    note.name = "Folded Note with Scribbles"

    # Display updated clue names
    print("\nUpdated clues:")
    print(key)
    print(puzzle_piece)
    print(note)

if __name__ == "__main__":
    main()
