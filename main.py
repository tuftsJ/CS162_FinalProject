from levels.villa.villa import VillaLevel

def main():
    print("Escape the Mystery Dungeon!\n")
    input("Hit enter to start.\n")

    level = VillaLevel()
    level.play()

if __name__ == "__main__":
    main()
