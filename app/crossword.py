from typing import List

from .word import Word


class Crossword:
    def __init__(self, words: List[str]):
        self.words = words
        self.remaining = words
        self.total_words = len(words)
        self.current_map = []

    def find_possible_maps(self):
        if len(self.current_map) == self.total_words:
            yield self.current_map.copy()

        words = self.remaining
        for i in range(len(words)):
            next_word = words[i]
            remaining = words[:i] + words[i + 1:]

            if len(self.current_map) == 0:
                yield from self.add_first_word(next_word, remaining)
            else:
                yield from self.add_next_word(next_word, remaining)

    def add_first_word(self, word: str, remaining: List[str]):
        new_word = Word(word, 0, 0, "h")
        self.current_map.append(new_word.to_dict())
        self.remaining = remaining
        yield from self.find_possible_maps()
        self.current_map.pop()  # Backtrack

    def add_next_word(self, next_word: str, remaining: List[str]):
        for item in self.current_map:
            word_object = Word(**item)
            for next_pos_x, next_pos_y, next_direction in self.calculate_next_position(word_object, next_word):
                if self.is_collision(word_object, next_word, next_pos_x, next_pos_y, next_direction):
                    continue

                new_word = Word(
                    next_word,
                    next_pos_x,
                    next_pos_y,
                    next_direction
                )
                self.current_map.append(new_word.to_dict())
                self.remaining = remaining
                yield from self.find_possible_maps()
                self.current_map.pop()  # Backtrack

    def calculate_next_position(self, word_object: Word, next_word: str):
        horizontal = word_object.direction == "h"
        for char_index, char in enumerate(word_object.word):
            if char in next_word:
                next_pos_x = char_index + \
                    word_object.pos_x if horizontal else word_object.pos_x - \
                    next_word.index(char)
                next_pos_y = word_object.pos_y + \
                    next_word.index(
                        char) if horizontal else word_object.pos_y - char_index
                next_direction = "v" if horizontal else "h"
                yield next_pos_x, next_pos_y, next_direction

    def is_collision(self, word_object: Word, next_word: str, next_pos_x: int, next_pos_y: int, next_direction: str) -> bool:
        filled_points = self.get_filled_points(word_object.word)
        next_word_filled_points = self.get_next_word_filled_points(
            next_word, next_pos_x, next_pos_y, next_direction)
        return len(filled_points.intersection(next_word_filled_points)) > 0

    def get_filled_points(self, target_word: str) -> set:
        filled_points = set()
        for item in self.current_map:
            if item['word'] == target_word:
                continue

            pos_x = item['pos_x']
            pos_y = item['pos_y']
            length = item['length']
            direction = item['direction']

            if direction == 'h':
                for x in range(pos_x, pos_x + length):
                    filled_points.add((x, pos_y))
                    # Add boundary points
                    filled_points.add((x, pos_y - 1))
                    filled_points.add((x, pos_y + 1))

                # Left and right boundaries
                filled_points.add((pos_x - 1, pos_y))
                filled_points.add((pos_x + length, pos_y))

            elif direction == 'v':
                for y in range(pos_y - length + 1, pos_y + 1):
                    filled_points.add((pos_x, y))
                    # Add boundary points
                    filled_points.add((pos_x - 1, y))
                    filled_points.add((pos_x + 1, y))

                # Upper and lower boundaries
                filled_points.add((pos_x, pos_y + 1))
                filled_points.add((pos_x, pos_y - length))

        return filled_points

    def get_next_word_filled_points(self, next_word: str, next_pos_x: int, next_pos_y: int, next_direction: str) -> set:
        next_word_filled_points = set()
        for i in range(len(next_word)):
            if next_direction == 'h':
                next_word_filled_points.add((next_pos_x + i, next_pos_y))
            else:
                next_word_filled_points.add((next_pos_x, next_pos_y - i))
        return next_word_filled_points

    def find_possible_maps_with_new_word(self, remaining: List[str]):
        self.words = remaining
        self.find_possible_maps()

    def print_current_map(self):
        print(self.current_map)
