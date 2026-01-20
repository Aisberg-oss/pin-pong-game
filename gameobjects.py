import pygame
pygame.init()

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
        self.speed_x = speed
        self.speed_y = speed
    def show_rect(self):
        self.window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def move_player1(self):
        button = pygame.key.get_pressed()
        if button[pygame.K_w] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if button[pygame.K_s] and self.rect.y <= 400:
            self.rect.y += self.speed
    def move_player2(self):
        button1 = pygame.key.get_pressed()
        if button1[pygame.K_UP] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if button1[pygame.K_DOWN] and self.rect.y <= 400:
            self.rect.y += self.speed

class Ball(GameSprite):
    def moving(self):
        self.rect.x -= self.speed_x
        self.rect.y -= self.speed_y
    def wall_touch(self):
        if self.rect.y <= 0:
            self.speed_y *= -1
        if self.rect.y >= 465:
            self.speed_y *= -1
    def platform_touch(self, platform1, platform2):
        if pygame.sprite.collide_rect(self, platform1):
            self.speed_x *= -1
        if pygame.sprite.collide_rect(self, platform2):
            self.speed_x *= -1
    def p_win(self, wind):
        font = pygame.font.Font(None, 70)
        p2_won = font.render('LEFT PLAYER WON', True, (0,0,0))
        p1_won = font.render('RIGHT PLAYER WON', True, (0, 0, 0))
        if self.rect.x < 0:
            wind.blit(p1_won, (0,250))
            return False
        if self.rect.x >= 500:
            wind.blit(p2_won, (0, 250))
            return False
        return True
