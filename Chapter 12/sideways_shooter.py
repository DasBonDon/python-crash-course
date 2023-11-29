# 12-6 Sideways Shooter
import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
SHIP_WIDTH, SHIP_HEIGHT = 50, 50
BULLET_WIDTH, BULLET_HEIGHT = 10, 5
WHITE = (255, 255, 255)
FPS = 60

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sideways Shooter")

# Load images
ship_img = pygame.Surface((SHIP_WIDTH, SHIP_HEIGHT))
ship_img.fill(WHITE)

# Define classes
class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = ship_img
        self.rect = self.image.get_rect()
        self.rect.topleft = (50, HEIGHT // 2 - SHIP_HEIGHT // 2)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((BULLET_WIDTH, BULLET_HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 7

    def update(self):
        self.rect.x += self.speed

# Create sprite groups
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# Create the player's ship
player = Ship()
all_sprites.add(player)

clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet(player.rect.right, player.rect.centery - 
                                BULLET_HEIGHT // 2)
                all_sprites.add(bullet)
                bullets.add(bullet)

    all_sprites.update()

    for bullet in bullets:
        if bullet.rect.x > WIDTH:
            bullet.kill()

    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()