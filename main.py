import pygame
from gameobjects import Player, Ball

window = pygame.display.set_mode((500, 500))
window.fill((200,200,200))
clock = pygame.time.Clock()

player1 = Player(50,50, 3, 'pictures/rocket.png', 50, 10, window)
player2 = Player(300,300, 3, 'pictures/rocket.png', 50, 10, window)
ball = Ball(100,100, 3, 'pictures/ball.png', 50, 10, window)

green_flag = True
while green_flag:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            green_flag = False
    pygame.display.update()
    clock.tick(50)
    #its a testing of the github so theres no game today
