import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner Game")
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)

sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()

score_surface = test_font.render("My Game", False, "black")
score_rect = score_surface.get_rect(center=(400, 50))

snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rectangle = snail_surface.get_rect(midbottom=(600, 300))

player_surface = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player_reactange = player_surface.get_rect(midbottom=(80, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEMOTION:
        #     # print(event.pos)
        #     if player_reactange.collidepoint(event.pos):
        #         print("Collision")

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    pygame.draw.rect(screen, "pink", score_rect)
    pygame.draw.rect(screen, "pink", score_rect, 10)
    screen.blit(score_surface, score_rect)

    if snail_rectangle.right <= 0:
        snail_rectangle.left = 800
    snail_rectangle.left -= 4
    screen.blit(snail_surface, snail_rectangle)
    screen.blit(player_surface, player_reactange)

    # if player_reactange.colliderect(snail_rectangle):
    #     print("Collision")

    # mouse_position = pygame.mouse.get_pos()
    # if player_reactange.collidepoint((mouse_position)):
    #     print(pygame.mouse.get_pressed())

    pygame.display.update()
    clock.tick(60)
