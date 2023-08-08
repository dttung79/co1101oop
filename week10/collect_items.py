import pygame
import sys
import random

class Ball:
    def __init__(self, position, radius, color):
        self.position = position
        self.radius = radius
        self.color = color

    def draw(self, window):
        pygame.draw.circle(window, self.color, self.position, self.radius)

class Item:
    def __init__(self, position, size, color):
        self.position = position
        self.size = size
        self.color = color

    def draw(self, window):
        pygame.draw.rect(window, self.color, pygame.Rect(*self.position, self.size, self.size))

class Game:
    def __init__(self, width=800, height=600):
        pygame.init()
        self.width, self.height = width, height
        self.window = pygame.display.set_mode((self.width, self.height))

        # Define some colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)

        # Define a list of 10 random colors
        self.colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(10)]

        # Initialize the ball and items
        self.ball = Ball([self.width // 2, self.height // 2], 15, self.RED)
        self.items = [Item([random.randint(50, self.width-50), random.randint(50, self.height-50)], 10, random.choice(self.colors)) for _ in range(10)]
        
        # Define constants for delay and move distance
        self.DELAY = 100  # delay in milliseconds
        self.MOVE_DISTANCE = 15  # move distance in pixels

        self.last_move = pygame.time.get_ticks()

    def draw_objects(self):
        self.ball.draw(self.window)
        for item in self.items:
            item.draw(self.window)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        now = pygame.time.get_ticks()
        if now - self.last_move > self.DELAY:
            if keys[pygame.K_UP]:
                self.ball.position[1] -= self.MOVE_DISTANCE
                self.last_move = now
            elif keys[pygame.K_DOWN]:
                self.ball.position[1] += self.MOVE_DISTANCE
                self.last_move = now
            elif keys[pygame.K_LEFT]:
                self.ball.position[0] -= self.MOVE_DISTANCE
                self.last_move = now
            elif keys[pygame.K_RIGHT]:
                self.ball.position[0] += self.MOVE_DISTANCE
                self.last_move = now
    def collide(self, ball, item):
        return abs(ball.position[0] - item.position[0]) < ball.radius + item.size // 2 and \
                abs(ball.position[1] - item.position[1]) < ball.radius + item.size // 2
    def check_collision(self):
        for item in self.items:
            if self.collide(self.ball, item):
                # change the color of the ball
                self.ball.color = item.color
                # increase the radius of the ball
                self.ball.radius += 3
                self.items.remove(item)

    def run(self):
        while True:
            self.handle_events()

            # Check for collisions between the ball and items
            self.check_collision()

            # Fill the window with black
            self.window.fill(self.BLACK)

            # Draw the ball and items
            self.draw_objects()

            # Update the display
            pygame.display.flip()

# Instantiate and run the game
game = Game()
game.run()
