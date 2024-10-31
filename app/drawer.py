from renderer import OutputRenderer, TerminalRenderer

from .word import Word


class Drawer:
    def __init__(self, words: list[Word] = [], renderer: OutputRenderer = TerminalRenderer()):
        self.renderer = renderer
        self.matrix = []
        self.x_offset = 0
        self.y_offset = 0
        self.width = 0
        self.height = 0

        self.set_words(words)

    def set_words(self, words: list[Word]):
        self.words = words
        if not words:
            return
        self.__calculate_dimensions()
        self.__create_matrix()
        self.__place_words()

    def __calculate_dimensions(self):
        self.min_x = min(w.pos_x for w in self.words)
        self.max_x = max(w.pos_x for w in self.words)
        self.min_y = min(w.pos_y for w in self.words)
        self.max_y = max(w.pos_y for w in self.words)

        self.x_offset = -self.min_x
        self.y_offset = -self.min_y

        filled_points = set()
        for word in self.words:
            for i in range(word.length):
                if word.direction == 'h':
                    filled_points.add((word.pos_x + i, word.pos_y))
                elif word.direction == 'v':
                    filled_points.add((word.pos_x, word.pos_y - i))
        leftmost = min(x for x, _ in filled_points)
        rightmost = max(x for x, _ in filled_points)
        topmost = max(y for _, y in filled_points)
        bottommost = min(y for _, y in filled_points)

        self.width = rightmost - leftmost + 1
        self.height = topmost - bottommost + 1

    def __create_matrix(self):
        self.matrix = [['.' for _ in range(self.width)]
                       for _ in range(self.height)]

    def __place_words(self):
        for word in self.words:
            adjusted_x = word.pos_x + self.x_offset
            adjusted_y = word.pos_y + self.y_offset

            for i in range(word.length):
                if word.direction == 'h':
                    self.matrix[self.max_y + self.y_offset -
                                adjusted_y][adjusted_x + i] = word.word[i]
                elif word.direction == 'v':
                    self.matrix[self.max_y + self.y_offset -
                                adjusted_y + i][adjusted_x] = word.word[i]

    def display(self):
        self.renderer.display(self.matrix)
