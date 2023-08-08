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
        self.BASKET_MOVE_DISTANCE = 1

        # Initialize the basket
        self.basket = Basket([self.width // 2, self.height - 50], self.BASKET_SIZE, self.WHITE)

        # Initialize the ball
        self.ball = Ball([random.randint(50, self.width-50), 0], self.BALL_RADIUS, self.WHITE, self.BALL_SPEED)

        # Initialize the score
        self.score = 0
        self.lives = 5

    def draw_objects(self):
        self.ball.draw(self.window)
        self.basket.draw(self.window)
        text = self.font.render("Score: " + str(self.score), 1, self.WHITE)
        self.window.blit(text, (10, 10))

        text_lives = self.font.render("Lives: " + str(self.lives), 1, self.WHITE)
        self.window.blit(text_lives, (10, 40))

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
        if self.is_out_of_bounds():
            self.ball = Ball([random.randint(50, self.width-50), 0], self.BALL_RADIUS, self.WHITE, self.BALL_SPEED)
        elif self.is_collided(self.ball, self.basket):
            self.ball = Ball([random.randint(50, self.width-50), 0], self.BALL_RADIUS, self.WHITE, self.BALL_SPEED)
            self.score += 1

    def is_out_of_bounds(self):
        if self.ball.position[1] > self.height:
            self.lives -= 1
            if self.lives == 0:
                print("Game over!")
                pygame.quit()
                sys.exit()
            return True
        return False
    
    def is_collided(self, ball, basket):
        if ball.position[0] + ball.radius < basket.position[0] or \
           ball.position[0] - ball.radius > basket.position[0] + basket.size[0] or \
           ball.position[1] + ball.radius < basket.position[1] or \
           ball.position[1] - ball.radius > basket.position[1] + basket.size[1]:
            return False
        if self.score > 0 and self.score % 3 == 0:
            self.BALL_SPEED += 0.2

        
        return True
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
