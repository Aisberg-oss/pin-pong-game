import pygame
from gameobjects import Player, Ball

window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

player1 = Player(10,50, 3, 'pictures/rocket.png', 20, 100, window)
player2 = Player(480,300, 3, 'pictures/rocket.png', 20, 100, window)
ball = Ball(250,250, 3, 'pictures/ball.png', 35, 35, window)

green_flag = True
while green_flag:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            green_flag = False
    clock.tick(50)
    player1.show_rect()
    player1.move_player1()
    player2.move_player2()
    player2.show_rect()
    ball.show_rect()
    ball.moving()
    ball.wall_touch()
    ball.platform_touch(player2, player1)
    pygame.display.update()
    ball.p_win(window)
    window.fill((200,200,200))
    #its a testing of the github so theres no game today
