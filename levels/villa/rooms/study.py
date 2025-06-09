# levels/villa/rooms/study.py

from levels.base_level import Room

class Study(Room):
    def __init__(self):
        self.room_item = "Ancient Key Fragment"
        name = "Study"
        description = (
            "A quiet room filled with books, a large desk, a painting, and an old globe.\n"
            "There's a faint smell of old parchment."
        )
        items = ["desk", "bookshelf", "painting", "globe", "drawer"]
        clues = ["desk", "bookshelf", "painting"]
        note_texts = {
            "desk": "You find a note taped under the desk: 'The first key lies where knowledge sleeps.'",
            "bookshelf": "A hidden bookmark reads: 'Seek the colors that tell the tale.'",
            "painting": "Behind the painting, a scribbled message: 'Light reveals the unseen.'"
        }

        super().__init__(name, description, items, clues, note_texts)
