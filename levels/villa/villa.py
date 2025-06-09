# levels/villa/villa.py

from levels.base_level import BaseLevel
from levels.villa.rooms.study import Study
from levels.villa.rooms.kitchen import Kitchen
from levels.villa.rooms.basement import Basement

class VillaLevel(BaseLevel):
    def __init__(self):
        intro_paragraph = (
            "The Villa is an old estate, abandoned for decades. Dusty furniture and ancient paintings\n"
            "line the halls, and each room holds fragments of your late professor’s past. Find the clues\n"
            "he left behind to uncover the truth and move forward on your journey."
        )
        rooms = [Study(), Kitchen(), Basement()]
        super().__init__("The Villa", intro_paragraph, rooms)
