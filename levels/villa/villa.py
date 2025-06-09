# levels/villa/villa.py

from levels.base_level import BaseLevel
from levels.villa.rooms.study import Study
from levels.villa.rooms.kitchen import Kitchen
from levels.villa.rooms.basement import Basement

class VillaLevel(BaseLevel):
    def __init__(self):
        rooms = [Study(), Kitchen(), Basement()]
        super().__init__("The Villa", rooms)
