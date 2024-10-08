import pygame

pygame.init()

screen = pygame.display.set_mode((1366,786))
clock = pygame.time.Clock()
player_pos = pygame.Vector2(screen.get_width() - (screen.get_width() - 70) , screen.get_height() - 70)
run = True
cooldown = 0
dt = 0

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill("black")


    pygame.draw.circle(screen, "white" , player_pos, 40)
    pygame.draw.aaline(screen, "white" , [0,screen.get_height() -50] , [screen.get_width(), screen.get_height() - 50])

    keys = pygame.key.get_pressed()

    if player_pos.y >= screen.get_height() - 90:
        player_pos.y = screen.get_height() - 90
    if player_pos.x >= screen.get_width() - 42:
        player_pos.x = screen.get_width() - 42 
    if player_pos.x <= 42:
        player_pos.x = 42
    
    cooldown -= 1

    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_ESCAPE]:
        run = False
    if keys[pygame.K_LSHIFT] and keys[pygame.K_w] and cooldown <= 0:
        player_pos.y -= 15000 * dt
        cooldown = 600
    if keys[pygame.K_LSHIFT] and keys[pygame.K_a] and cooldown <= 0:
        player_pos.x -= 12500 * dt
        cooldown = 600
    if keys[pygame.K_LSHIFT] and keys[pygame.K_s] and cooldown <= 0:
        player_pos.y += 7000 * dt
        cooldown = 600
    if keys[pygame.K_LSHIFT] and keys[pygame.K_d] and cooldown <= 0:
        player_pos.x += 9500 * dt
        cooldown = 600

    pygame.display.flip()

    dt = clock.tick(120) / 1000

pygame.quit()