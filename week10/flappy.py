import pygame
import sys
import random

class Bird:
    def __init__(self, position, size, color, speed):
        self.position = position
        self.size = size
        self.color = color
        self.speed = speed

    def draw(self, window):
        pygame.draw.rect(window, self.color, pygame.Rect(*self.position, *self.size))

    def move(self, direction):
        self.position[1] += self.speed * direction

class Pillar:
    def __init__(self, position, size, color, speed):
        self.position = position
        self.size = size
        self.color = color
        self.speed = speed

    def draw(self, window):
        pygame.draw.rect(window, self.color, pygame.Rect(*self.position, *self.size))

    def move(self):
        self.position[0] -= self.speed

class Game:
    def __init__(self, width=800, height=600):
        pygame.init()
        self.width, self.height = width, height
        self.window = pygame.display.set_mode((self.width, self.height))
        self.font = pygame.font.Font(None, 36)

        # Define some colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)

        # Initialize the bird and pillars
        self.bird = Bird([self.width // 2, self.height // 2], [20, 20], self.WHITE, 4)
        self.pillars = []

        # Initialize the score
        self.score = 0

    def draw_objects(self):
        self.bird.draw(self.window)
        for pillar in self.pillars:
            pillar.draw(self.window)
        text = self.font.render("Score: " + str(self.score), 1, self.WHITE)
        self.window.blit(text, (10, 10))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.bird.move(-1)
        elif keys[pygame.K_DOWN]:
            self.bird.move(1)

    def check_collision(self):
        for pillar in self.pillars:
            if (self.bird.position[0] < pillar.position[0] + pillar.size[0] and
                self.bird.position[0] + self.bird.size[0] > pillar.position[0] and
                self.bird.position[1] < pillar.position[1] + pillar.size[1] and
                self.bird.position[1] + self.bird.size[1] > pillar.position[1]):
                return True
        return False

    def add_pillar(self):
        hole_size = random.randint(150, 250)
        hole_position = random.randint(50, self.height - 50 - hole_size)
        self.pillars.append(Pillar([self.width, 0], [80, hole_position], self.WHITE, 4))
        self.pillars.append(Pillar([self.width, hole_position + hole_size], [80, self.height - hole_position - hole_size], self.WHITE, 4))

    def update_pillars(self):
        for pillar in self.pillars:
            pillar.move()
            if pillar.position[0] + pillar.size[0] < 0:
                self.pillars.remove(pillar)
                self.score += 0.5

    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            self.handle_events()

            # Check for collisions between the bird and pillars
            if self.check_collision():
                break

            # Fill the window with black
            self.window.fill(self.BLACK)

            # Draw the bird and pillars
            self.draw_objects()

            # Update the pillars
            self.update_pillars()

            # Add new pillars
            if len(self.pillars) == 0 or self.pillars[-1].position[0] < self.width - 200:
                self.add_pillar()

            # Update the display
            pygame.display.flip()

        print("Game Over!")

# Instantiate and run the game
game = Game()
game.run()
