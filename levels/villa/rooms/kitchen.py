# levels/villa/rooms/kitchen.py

from levels.base_level import Room

class Kitchen(Room):
    def __init__(self):
        self.room_item = "Silver Compass Piece"
        name = "Kitchen"
        description = (
            "A large kitchen with shining pots, a locked cabinet, a rusty knife block,\n"
            "and a mysterious spice rack."
        )
        items = ["cabinet", "fridge", "knife block", "spice rack", "table"]
        clues = ["cabinet", "spice rack", "knife block"]
        note_texts = {
            "cabinet": "A note inside says: 'The flavors of the past hold a secret.'",
            "spice rack": "You find a hidden message: 'The heat will reveal the truth.'",
            "knife block": "A carved inscription reads: 'Sharp eyes find sharp clues.'"
        }

        super().__init__(name, description, items, clues, note_texts)
