from levels.villa.villa import VillaLevel

def main():
    print(" ")
    print("Escape the Mystery Dungeon!\n")

    print("Your former teacher has left. You have no idea where they have gone. They left a note:\n"
          "Dear student, I have left on an adventure of a lifetime. I have taught you everything\n"
          "I know. I hope you can forgive me for leaving without a trace. IF you have learned what\n"
          "I have to teach, you will be able to follow and find me at my goal...\n")

    print("Enter if you dare! You will be tested to your limits!\n")

    print("Each level will contain three rooms. Each room three clues. Each time you find\n"
          "a clue it will lead you to the next clue. After you collected all clues in the room you will\n"
          "move onto the next room. Once you have found all the clues and 3 items, you will complete the level\n"
          "and move onto the next level. One step closer to finding your former teacher.\n")

    input("Hit enter to start.\n")

    level = VillaLevel()
    level.play()

if __name__ == "__main__":
    main()
