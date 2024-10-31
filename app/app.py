from .crossword import Crossword
from .drawer import Drawer
from .word import Word

from ui import UIManager, RendererType


class CrosswordApp:
    def __init__(self, words, renderer=RendererType.TERMINAL):
        self.words = words
        self.crossword = Crossword(words)
        self.possible_maps = self.crossword.find_possible_maps()
        self.ui_manager = UIManager(words, renderer)
        self.drawer = Drawer(renderer=self.ui_manager.renderer)

    def run(self):
        self.ui_manager.run(self)

    def process_next_map(self):
        try:
            words_data = next(self.possible_maps)
            self.drawer.set_words([Word(**data) for data in words_data])
            self.drawer.display()
        except StopIteration:
            print(" -> All possible maps are displayed.\n")
            self.reset_crossword()

    def process_all_maps(self):
        total_maps = 0
        for words_data in self.possible_maps:
            self.drawer.set_words([Word(**data) for data in words_data])
            self.drawer.display()
            total_maps += 1
            print("\n")

        print(f" -> Total maps: {total_maps}\n")

    def reset_crossword(self):
        self.crossword = Crossword(self.words)
        self.possible_maps = self.crossword.find_possible_maps()
        self.process_next_map()
