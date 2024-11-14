import pygame
from sys import exit
from random import randint

def display_score():
    current_time = int((pygame.time.get_ticks() - start_time) / 1000)
    score_surface = test_font.render(f"Score: {current_time}", False, (64, 64, 64))
    score_rect = score_surface.get_rect(center=(400, 50))
    screen.blit(score_surface, score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5
            if obstacle_rect.right <= 0:
                obstacle_list.remove(obstacle_rect)
            screen.blit(snail_surface, obstacle_rect)
        return obstacle_list
    else:
        return []

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner Game")
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)
game_active = False
start_time = 0
score = 0

# Surfaces
game_title = test_font.render("Running Man", False, (111, 196, 169))
game_title_rect = game_title.get_rect(center=(400, 50))

instructions_surface = test_font.render("Press Space to Run", False, (111, 196, 169))
instructions_rect = instructions_surface.get_rect(center=(400, 340))

sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()

# Obstacles
snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rectangle = snail_surface.get_rect(midbottom=(600, 300))

obstacle_rect_list = []

player_surface = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player_reactange = player_surface.get_rect(midbottom=(80, 300))
player_gravity = 0

# Introduction Screen
player_stand = pygame.image.load("graphics/Player/player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rectangle = player_stand.get_rect(center=(400, 200))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:

            if event.type == pygame.MOUSEBUTTONDOWN and player_reactange.bottom >= 300:
                if player_reactange.collidepoint(event.pos):
                    player_gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_reactange.bottom >= 300:
                    player_gravity = -20

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rectangle.left = 800
                start_time = pygame.time.get_ticks()

        if event.type == obstacle_timer and game_active:
            obstacle_rect_list.append(snail_surface.get_rect(bottomright=(randint(900, 1100), 300)))

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        # pygame.draw.rect(screen, "#c0e8ec", score_rect)
        # pygame.draw.rect(screen, "#c0e8ec", score_rect, 10)
        # screen.blit(score_surface, score_rect)
        score = display_score()

        # Player
        player_gravity += 1
        player_reactange.bottom += player_gravity
        if player_reactange.bottom >= 300:
            player_reactange.bottom = 300
        screen.blit(player_surface, player_reactange)

        # Obstacles
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # Collision
        if player_reactange.colliderect(snail_rectangle):
            game_active = False
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rectangle)

        score_message = test_font.render(f"Your Score: {score}", False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center=(400, 340))
        screen.blit(game_title, game_title_rect)

        if score == 0:
            screen.blit(instructions_surface, instructions_rect)
        else:
            screen.blit(score_message, score_message_rect)

    pygame.display.update()
    clock.tick(60)
