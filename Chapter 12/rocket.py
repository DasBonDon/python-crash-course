# Class for 12-4
import pygame

class Rocket:
    def __init__(self, bs_game, width, height):
        self.screen = bs_game.screen
        self.screen_rect = bs_game.screen.get_rect()

        self.original_image = pygame.image.load('Chapter 12/images/rocket.bmp')
        self.original_rect = self.original_image.get_rect()

        self.image = pygame.transform.scale(self.original_image, 
                                            (width, height))
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

        # Store a float for the ship's exact position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flag; start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        # Update the rocket's position based on movement flags.
        # Update the rocket's x and y values, and then update the rect.

        self.rocket_speed = 3

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.rocket_speed
        # Use rect.top to check the top edge
        if self.moving_up and self.rect.top > 0:
            self.y -= self.rocket_speed
        # Use rect.bottom to check the bottom edge
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.rocket_speed

        # Update the rect object based on the updated x and y values
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)