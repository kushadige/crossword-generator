from enum import Enum


class OutputRenderer:
    def run(self, app):
        raise NotImplementedError(
            "This method should be implemented by subclasses."
        )

    def display(self, matrix):
        raise NotImplementedError(
            "This method should be implemented by subclasses."
        )


class RendererType(Enum):
    TERMINAL = 'terminal'
    PYGAME = 'pygame'
