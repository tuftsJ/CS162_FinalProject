# levels/villa/rooms/basement.py

from levels.base_level import Room

class Basement(Room):
    def __init__(self):
        self.room_item = "Golden Locket"
        name = "Basement"
        description = (
            "A dark, musty basement with wooden crates, a broken lantern, old wine bottles,\n"
            "and cobweb-covered shelves."
        )
        items = ["wooden crate", "lantern", "wine bottles", "shelves", "old chest"]
        clues = ["wooden crate", "lantern", "old chest"]
        note_texts = {
            "wooden crate": "A scratched note: 'Where treasures rest under the floor.'",
            "lantern": "The lantern's glass holds a faint engraving: 'Light guides the way.'",
            "old chest": "Inside the chest, a faded map points to the garden maze."
        }

        super().__init__(name, description, items, clues, note_texts)
