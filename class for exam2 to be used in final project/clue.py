# clue.py

class Clue:
    def __init__(self, name):
        self._name = name  # Protected attribute

    @property
    def name(self):
        """Get the name of the clue"""
        return self._name

    @name.setter
    def name(self, value):
        """Set the name of the clue"""
        if not isinstance(value, str):
            raise ValueError("Clue name must be a string.")
        self._name = value

    def __str__(self):
        return f"Clue: {self._name}"
