import pygame
import sys

class Renderer:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Renderer")

    def draw_rect(self, x, y, width, height, color):
        pygame.draw.rect(self.screen, color, (x, y, width, height))

    def draw_circle(self, x, y, radius, color):
        pygame.draw.circle(self.screen, color, (x, y), radius)

    def draw_image(self, image, x, y):
        self.screen.blit(image, (x, y))

    def clear(self):
        self.screen.fill((0, 0, 0))

    def update(self):
        pygame.display.flip()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.clear()
            # Add your rendering code here
            self.update()
        pygame.quit()

if __name__ == "__main__":
    renderer = Renderer(800, 600)

    while True:
        renderer.draw_rect(100, 100, 50, 50, (255, 0, 0))
        renderer.draw_circle(200, 200, 30, (0, 0, 255))
        renderer.update()
