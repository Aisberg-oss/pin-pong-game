class GameSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, image, w, h, window):
        super().__init__()
        self.window = window
        self.image = pygame.transform.scale(pygame.image.load(image), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.h = h
        self.speed = speed
    def show_rect(self):
        self.window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def move_player1(self):
        button = key.get_pressed()
        if button[K_w]:
            self.rect.y -= self.speed
        if button[K_s]:
            self.rect.y += self.speed
    def move_player2(self):
        button1 = key.get_pressed()
        if button1[K_UP]:
            self.rect.y -= self.speed
        if button1[K_DOWN]:
            self.rect.y += self.speed

class Ball(GameSprite):
    def moving(self):
        self.rect.x -= self.speed
        self.rect.y -= self.speed
    def wall_touch(self):
        if self.rect.y >= 500:
            self.rect.y -= self.speed
            self.rect.x -= self.speed
        if self.rect.y <= 500:
            self.rect.y += self.speed
            self.rect.x += self.speed
    def platform_touch(self, platform1, platform2):
        if sprite.spritecollide(self, platform1, False):
            self.rect.x += self.speed
            self.rect.y += self.speed
        if sprite.spritecollide(self, platform2, False):
            self.rect.x -= self.speed
            self.rect.y -= self.speed