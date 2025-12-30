import pygame

window = pygame.display.set_mode((500, 500))
window.fill((200,200,200))
clock = pygame.time.Clock()

green_flag = True
while green_flag:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            green_flag = False
    pygame.display.update()
    clock.tick(50)