import pygame
from .output_renderer import OutputRenderer


class PygameRenderer(OutputRenderer):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()

    def run(self, app):
        app.process_next_map()  # First map
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        app.process_next_map()

            self.clock.tick(60)

    def display(self, matrix):
        bg_color = (255, 255, 255)
        self.screen.fill(bg_color)

        cell_size = 45
        container_width = len(matrix[0]) * cell_size
        container_height = len(matrix) * cell_size
        container = pygame.Surface((container_width, container_height))
        container.fill(bg_color)

        for y, row in enumerate(matrix):
            for x, cell in enumerate(row):
                if cell != '.':
                    text_surface = pygame.Surface((cell_size, cell_size))
                    text_surface.fill((250, 200, 0))
                    text_surface_rect = text_surface.get_rect()
                    pygame.draw.rect(
                        text_surface, bg_color, text_surface_rect, 1, 1
                    )

                    text = self.render_text(cell)
                    text_rect = text.get_rect(center=text_surface_rect.center)
                    text_surface.blit(text, text_rect)

                    container.blit(
                        text_surface, (x * cell_size, y * cell_size)
                    )

        # Container
        screen_rect = self.screen.get_rect()
        container_rect = container.get_rect(center=screen_rect.center)
        self.screen.blit(container, container_rect)

        # Title
        title_font = pygame.font.Font(None, 48)
        title_surface = title_font.render(
            "Crossword Puzzle", True, (0, 0, 0))
        title_rect = title_surface.get_rect(
            center=(screen_rect.centerx, screen_rect.top + 30))
        self.screen.blit(title_surface, title_rect)

        # Info
        info_font = pygame.font.Font(None, 36)
        info_surface = info_font.render(
            "Press Enter to generate new map", True, (0, 0, 0))
        info_rect = info_surface.get_rect(
            center=(screen_rect.centerx, screen_rect.bottom - 30))
        self.screen.blit(info_surface, info_rect)

        pygame.display.flip()

    def render_text(self, char):
        font = pygame.font.Font(None, 36)
        text = font.render(char, True, (0, 0, 0))
        return text
