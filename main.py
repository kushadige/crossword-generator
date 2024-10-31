import os
import argparse
from app import CrosswordApp
from renderer import RendererType


def main():
    parser = argparse.ArgumentParser(
        description="Crossword Puzzle Application")
    parser.add_argument("-f", "--file", type=str,
                        help="Input file containing words")
    parser.add_argument("-r", "--renderer", type=str, choices=['pygame', 'terminal'],
                        help="Renderer type (pygame/terminal)")
    args = parser.parse_args()

    # Words input
    if args.file:
        if os.path.isfile(args.file):
            with open(args.file, 'r') as f:
                words = [word.strip().upper() for word in f.read().split()]
        else:
            print(f"File -> `{args.file}` does not exist.")
            return
    else:
        words_input = input("Enter the words (separated by space): ")
        words = [word.upper() for word in words_input.split(" ") if word]

        if not words:
            print("No words entered.")
            return

    # Renderer type selection
    if args.renderer:
        renderer_type = RendererType.PYGAME if args.renderer == 'pygame' else RendererType.TERMINAL
    else:
        renderer_type_input = input(
            "Enter the renderer type (pygame/terminal) - optional: ")
        renderer_type = RendererType.PYGAME if renderer_type_input.lower(
        ) == "pygame" else RendererType.TERMINAL

    app = CrosswordApp(words, renderer_type)
    app.run()


if __name__ == "__main__":
    main()
