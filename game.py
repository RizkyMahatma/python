import pygame
import random
 
pygame.init()
 
# Lebar dan tinggi layar
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
 
# Warna dasar
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
 
# Inisialisasi layar
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Genshin Lite")
 
# Kelas pemain
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
 
    # Gerak pemain
    def update(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.rect.x -= 5
        if keystate[pygame.K_RIGHT]:
            self.rect.x += 5
        if keystate[pygame.K_UP]:
            self.rect.y -= 5
        if keystate[pygame.K_DOWN]:
            self.rect.y += 5
 
# Kelas musuh
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(SCREEN_HEIGHT - self.rect.height)
 
# Grup sprite
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
 
# Menambahkan sprite
player = Player()
all_sprites.add(player)
 
for i in range(5):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)
 
# Loop permainan
done = False
clock = pygame.time.Clock()
 
while not done:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # Update sprite
    all_sprites.update()
 
    # Cek tabrakan
    hits = pygame.sprite.spritecollide(player, enemies, False)
    if hits:
        done = True
 
    # Rendering
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()
