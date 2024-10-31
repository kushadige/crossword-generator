import sys
from select import select

from .output_renderer import OutputRenderer


class TerminalRenderer(OutputRenderer):
    def run(self, app):
        print("\n")
        print("-" * 20)
        print(" Crossword Puzzle")
        print("-" * 20)
        print("\n -> Press Enter to generate next map. Type 'exit' to quit.\n")
        app.process_next_map()  # First map is displayed at the beginning
        while True:
            command = self.get_command()
            if not self.process_command(command, app):
                break

    def display(self, matrix):
        for row in matrix:
            print(' '.join(row))

    def get_command(self):
        rlist, _, _ = select([sys.stdin], [], [], 1)
        if rlist:
            return input()
        return None

    def process_command(self, command, app):
        if command == "exit":
            return False
        elif command == "":
            app.process_next_map()
        return True
