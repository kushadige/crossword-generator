from typing import Any, Dict


class Word:
    def __init__(self, word: str, pos_x: int, pos_y: int, direction: str, **kwargs):
        self.word = word
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.direction = direction
        self.length = len(word)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "word": self.word,
            "pos_x": self.pos_x,
            "pos_y": self.pos_y,
            "direction": self.direction,
            "length": self.length
        }
