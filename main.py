import pygame

pygame.init()

# вікно створити
window = pygame.display.set_mode((700, 500))
fps = pygame.time.Clock()



class Sprite:
    def __init__(self, speed, spriteName, x, y, w, h):
        self.image = pygame.transform.scale(pygame.image.load(spriteName), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def draw(self, window):
        window.blit(self.image, [self.rect.x, self.rect.y])


class Player(Sprite):
    def __init__(self, x, y, filename, speed, w, h):
        super().__init__(x, y, filename, speed, w, h)
        self.patrons = []

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            #if self.rect.y < 400:
            self.rect.y -= self.speed

        if keys[pygame.K_s]:
            #if self.rect.y < 5:
            self.rect.y += self.speed
    def draw(self, window):
        window.blit(self.image, [self.rect.x, self.rect.y])
        super(Player, self).draw(window)



player = Player(7, "platf.png", 0, 385, 50, 110)
background = pygame.transform.scale(pygame.image.load("sky.png"), (700, 500))


game = True
while game:
    # обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    # оновлення
    player.update()
    # відмалювання
    window.blit(background, [0, 0])
    player.draw(window)
    pygame.display.flip()
    fps.tick(60)