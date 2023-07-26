import pygame
import sys
import random

class Ball:
    def __init__(self, position, radius, color, speed):
        self.position = position
        self.radius = radius
        self.color = color
        self.speed = speed

    def draw(self, window):
        pygame.draw.circle(window, self.color, self.position, self.radius)

    def move(self):
        self.position[1] += self.speed

class Basket:
    def __init__(self, position, size, color):
        self.position = position
        self.size = size
        self.color = color

    def draw(self, window):
        pygame.draw.rect(window, self.color, pygame.Rect(*self.position, *self.size))

class Game:
    def __init__(self, width=800, height=600):
        pygame.init()
        self.width, self.height = width, height
        self.window = pygame.display.set_mode((self.width, self.height))
        self.font = pygame.font.Font(None, 36)

        # Define some constants
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.BALL_RADIUS = 15
        self.BALL_SPEED = 0.5
        self.BASKET_SIZE = [100, 20]
        self.BASKET_MOVE_DISTANCE = 5

        # Initialize the basket
        self.basket = Basket([self.width // 2, self.height - 50], self.BASKET_SIZE, self.WHITE)

        # Initialize the ball
        self.ball = Ball([random.randint(50, self.width-50), 0], self.BALL_RADIUS, self.WHITE, self.BALL_SPEED)

        # Initialize the score
        self.score = 0

    def draw_objects(self):
        self.ball.draw(self.window)
        self.basket.draw(self.window)
        text = self.font.render("Score: " + str(self.score), 1, self.WHITE)
        self.window.blit(text, (10, 10))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.basket.position[0] -= self.BASKET_MOVE_DISTANCE
        if keys[pygame.K_RIGHT]:
            self.basket.position[0] += self.BASKET_MOVE_DISTANCE

    def check_collision(self):
        self.ball.move()
        if self.ball.position[1] > self.height:
            self.ball = Ball([random.randint(50, self.width-50), 0], self.BALL_RADIUS, self.WHITE, self.BALL_SPEED)
        elif abs(self.basket.position[0] - self.ball.position[0]) < self.basket.size[0] // 2 and \
             abs(self.basket.position[1] - self.ball.position[1]) < self.basket.size[1] // 2:
            self.ball = Ball([random.randint(50, self.width-50), 0], self.BALL_RADIUS, self.WHITE, self.BALL_SPEED)
            self.score += 1

    def run(self):
        while True:
            self.handle_events()

            # Check for collisions between the basket and the ball
            self.check_collision()

            # Fill the window with black
            self.window.fill(self.BLACK)

            # Draw the ball and basket
            self.draw_objects()

            # Update the display
            pygame.display.flip()

# Instantiate and run the game
game = Game()
game.run()
