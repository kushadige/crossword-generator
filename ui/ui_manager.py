from renderer import TerminalRenderer, RendererType


class UIManager:
    def __init__(self, words, renderer_type=RendererType.TERMINAL):
        self.words = words
        self.renderer = self.create_renderer(renderer_type)

    def create_renderer(self, renderer_type):
        if renderer_type == RendererType.TERMINAL:
            return TerminalRenderer()
        elif renderer_type == RendererType.PYGAME:
            from renderer.pygame_renderer import PygameRenderer
            return PygameRenderer()
        else:
            raise ValueError("Invalid renderer type.")

    def run(self, app):
        self.renderer.run(app)
