import pygame
import sys

class Game:
    def __init__(self, width=800, height=600, square_size=50):
        pygame.init()
        self.width, self.height = width, height
        self.square_size = square_size
        self.window = pygame.display.set_mode((self.width, self.height))

        # Define some colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)

        # Initialize the square's position at the center of the window
        self.square_position = [self.width // 2, self.height // 2]

        # Define step size for square's movement
        self.step_size = [10, 10]  # Adjust these values as needed

    def draw_square(self):
        pygame.draw.rect(self.window, self.WHITE, 
                         pygame.Rect(*self.square_position, self.square_size, self.square_size))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.square_position[1] -= self.step_size[1]
                elif event.key == pygame.K_DOWN:
                    self.square_position[1] += self.step_size[1]

    def run(self):
        while True:
            self.handle_events()

            # Fill the window with black
            self.window.fill(self.BLACK)

            # Draw the square
            self.draw_square()

            # Update the display
            pygame.display.flip()

# Instantiate and run the game
game = Game()
game.run()
